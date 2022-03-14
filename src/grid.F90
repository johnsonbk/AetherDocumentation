module grid

integer, parameter, public :: max_hcoordname_len   = 16
integer, parameter, public :: max_chars = 256
integer, parameter, public :: iMap = 1
! Note from Ben: figure out what the correct numbers are from use dimensions_mod,         only: np, nc, npsq, nlev, nlevp, qsize_d, max_neigh_edges,ntrac_d
integer, parameter, public :: np = 48602
integer, parameter, public :: npsq = 48602*48602
integer, parameter, public :: nelemd = 48602
integer, parameter, public :: qsize_d = 6

integer, public, parameter :: num_neighbors=8 ! for north, south, east, west, neast, nwest, seast, swest

integer, parameter, public :: nlev = 45
integer, parameter, public :: nlevp=nlev+1
integer, public, parameter :: timelevels = 3

! From shr_kind_mod.F90
integer,parameter :: i4 = selected_int_kind (6) ! 4 byte integer
integer,parameter :: i8 = selected_int_kind (13) ! 8 byte integer
integer, parameter, public :: r8 = selected_real_kind(12)

! From /cam/src/dynamics/se/dycore/coordinate_systems_mod.F90
type, public :: cartesian2D_t
      real(r8) :: x             ! x coordinate
      real(r8) :: y             ! y coordinate
end type cartesian2D_t

type, public :: cartesian3D_t
  real(r8) :: x             ! x coordinate
  real(r8) :: y             ! y coordinate
  real(r8) :: z             ! z coordinate
end type cartesian3D_t

type, public :: spherical_polar_t
  real(r8) :: r             ! radius
  real(r8) :: lon           ! longitude
  real(r8) :: lat           ! latitude
end type spherical_polar_t

! From gridgraph_mod.F90
type, public :: GridVertex_t 
    integer, pointer          :: nbrs(:) => null()           ! The numbers of the neighbor elements
    integer, pointer          :: nbrs_face(:) => null()      ! The cube face number of the neighbor element (nbrs     array)
    integer, pointer          :: nbrs_wgt(:) => null()       ! The weights for edges defined by nbrs array
    integer, pointer          :: nbrs_wgt_ghost(:) => null() ! The weights for edges defined by nbrs array
    integer                   :: nbrs_ptr(num_neighbors + 1) !index into the nbrs array for each neighbor direction

    integer                   :: face_number           ! which face of the cube this vertex is on
    integer                   :: number                ! element number
    integer                   :: processor_number      ! processor number
    integer                   :: SpaceCurve  ! index in Space-Filling curve
end type GridVertex_t

!  edgetype_mod.F90
type, public :: rotation_t
  integer                 :: nbr                ! nbr direction: north south east west
  integer                 :: reverse            ! 0 = do not reverse order
  ! 1 = reverse order
  real (kind=r8), pointer :: R(:,:,:) => null() !  rotation matrix
end type rotation_t

type, public :: EdgeDescriptor_t
  integer                      :: use_rotation
  integer                      :: padding
  integer,             pointer :: putmapP(:) => null()
  integer,             pointer :: getmapP(:) => null()
  integer,             pointer :: putmapP_ghost(:) => null()
  integer,             pointer :: getmapP_ghost(:) => null()
  integer,             pointer :: putmapS(:) => null()
  integer,             pointer :: getmapS(:) => null()
  integer,             pointer :: globalID(:) => null()
  integer,             pointer :: loc2buf(:) => null()
  type(cartesian3D_t), pointer :: neigh_corners(:,:) => null()
  integer                      :: actual_neigh_edges
  logical,             pointer :: reverse(:) => null()
  type (rotation_t),   pointer :: rot(:) => null() !  Identifies list of edges
  !  that must be rotated, and how
end type EdgeDescriptor_t

!---------------------------------------------------------------------------
!
!  horiz_coord_t: Information for horizontal dimension attributes
!
!---------------------------------------------------------------------------

! use element_mod,            only: element_t
! =========== PRIMITIVE-EQUATION DATA-STRUCTURES =====================

type, public :: elem_state_t

! prognostic variables for preqx solver

! prognostics must match those in prim_restart_mod.F90
! vertically-lagrangian code advects dp3d instead of ps
! tracers Q, Qdp always use 2 level time scheme

real (kind=r8) :: v     (np,np,2,nlev,timelevels)            ! velocity                           
real (kind=r8) :: T     (np,np,nlev,timelevels)              ! temperature                        
real (kind=r8) :: dp3d  (np,np,nlev,timelevels)              ! dry delta p on levels              
real (kind=r8) :: psdry (np,np)                              ! dry surface pressure               
real (kind=r8) :: phis  (np,np)                              ! surface geopotential (prescribed)  
real (kind=r8) :: Qdp   (np,np,nlev,qsize_d,2)               ! Tracer mass                        

end type elem_state_t

!___________________________________________________________________
type, public :: derived_state_t
 !
 ! storage for subcycling tracers/dynamics
 !
real (kind=r8) :: vn0  (np,np,2,nlev)                      ! velocity for SE tracer advection
real (kind=r8) :: dpdiss_biharmonic(np,np,nlev)            ! mean dp dissipation tendency, if nu_p>0
real (kind=r8) :: dpdiss_ave(np,np,nlev)                   ! mean dp used to compute psdiss_tens

! diagnostics for explicit timestep
real (kind=r8) :: phi(np,np,nlev)                          ! geopotential
real (kind=r8) :: omega(np,np,nlev)                        ! vertical velocity

! semi-implicit diagnostics: computed in explict-component, reused in Helmholtz-component.
real (kind=r8) :: zeta(np,np,nlev)                         ! relative vorticity
real (kind=r8) :: div(np,np,nlev,timelevels)               ! divergence

! tracer advection fields used for consistency and limiters
real (kind=r8) :: dp(np,np,nlev)                           ! for dp_tracers at physics timestep
real (kind=r8) :: divdp(np,np,nlev)                        ! divergence of dp
real (kind=r8) :: divdp_proj(np,np,nlev)                   ! DSSed divdp
real (kind=r8) :: mass(MAX(qsize_d,ntrac_d)+9)             ! total tracer mass for diagnostics

! forcing terms for CAM
real (kind=r8) :: FQ(np,np,nlev,qsize_d)                   ! tracer forcing
real (kind=r8) :: FM(np,np,2,nlev)                         ! momentum forcing
real (kind=r8) :: FDP(np,np,nlev)                          ! save full updated dp right after physics
real (kind=r8) :: FT(np,np,nlev)                           ! temperature forcing
real (kind=r8) :: etadot_prescribed(np,np,nlevp)           ! prescribed vertical tendency
real (kind=r8) :: u_met(np,np,nlev)                        ! zonal component of prescribed meteorology winds
real (kind=r8) :: dudt_met(np,np,nlev)                     ! rate of change of zonal component of prescribed meteorology winds
real (kind=r8) :: v_met(np,np,nlev)                        ! meridional component of prescribed meteorology winds
real (kind=r8) :: dvdt_met(np,np,nlev)                     ! rate of change of meridional component of prescribed meteorology winds
real (kind=r8) :: T_met(np,np,nlev)                        ! prescribed meteorology temperature
real (kind=r8) :: dTdt_met(np,np,nlev)                     ! rate of change of prescribed meteorology temperature
real (kind=r8) :: ps_met(np,np)                            ! surface pressure of prescribed meteorology
real (kind=r8) :: dpsdt_met(np,np)                         ! rate of change of surface pressure of prescribed meteorology
real (kind=r8) :: nudge_factor(np,np,nlev)                 ! nudging factor (prescribed)
real (kind=r8) :: Utnd(npsq,nlev)                          ! accumulated U tendency due to nudging towards prescribed met
real (kind=r8) :: Vtnd(npsq,nlev)                          ! accumulated V tendency due to nudging towards prescribed met
real (kind=r8) :: Ttnd(npsq,nlev)                          ! accumulated T tendency due to nudging towards prescribed met

real (kind=r8) :: pecnd(np,np,nlev)                        ! pressure perturbation from condensate

end type derived_state_t

!___________________________________________________________________
type, public :: elem_accum_t


! the "4" timelevels represents data computed at:
!  1  t-.5
!  2  t+.5   after dynamics
!  3  t+.5   after forcing
!  4  t+.5   after Robert
! after calling TimeLevelUpdate, all times above decrease by 1.0


end type elem_accum_t


! ============= DATA-STRUCTURES COMMON TO ALL SOLVERS ================

type, public :: index_t
 integer :: ia(npsq),ja(npsq)
 integer :: is,ie
 integer :: NumUniquePts
 integer :: UniquePtOffset
end type index_t

!___________________________________________________________________
type, public :: element_t
 integer :: LocalId
 integer :: GlobalId

 ! Coordinate values of element points
 type (spherical_polar_t) :: spherep(np,np)                       ! Spherical coords of GLL points

 ! Equ-angular gnomonic projection coordinates
 type (cartesian2D_t)     :: cartp(np,np)                         ! gnomonic coords of GLL points
 type (cartesian2D_t)     :: corners(4)                           ! gnomonic coords of element corners
 real (kind=r8)    :: u2qmap(4,2)                          ! bilinear map from ref element to quad in cubedsphere coordinates
                                                                  ! SHOULD BE REMOVED
 ! 3D cartesian coordinates
 type (cartesian3D_t)     :: corners3D(4)

 ! Element diagnostics
 real (kind=r8)    :: area                                 ! Area of element
 real (kind=r8)    :: normDinv                             ! some type of norm of Dinv used for CFL
 real (kind=r8)    :: dx_short                             ! short length scale in km
 real (kind=r8)    :: dx_long                              ! long length scale in km

 real (kind=r8)    :: variable_hyperviscosity(np,np)       ! hyperviscosity based on above
 real (kind=r8)    :: hv_courant                           ! hyperviscosity courant number
 real (kind=r8)    :: tensorVisc(np,np,2,2)                !og, matrix V for tensor viscosity

 ! Edge connectivity information
!     integer :: node_numbers(4)
!     integer :: node_multiplicity(4)                 ! number of elements sharing corner node

 type (GridVertex_t)      :: vertex                               ! element grid vertex information
 type (EdgeDescriptor_t)  :: desc

 type (elem_state_t)      :: state

 type (derived_state_t)   :: derived
 ! Metric terms
 real (kind=r8)    :: met(np,np,2,2)                       ! metric tensor on velocity and pressure grid
 real (kind=r8)    :: metinv(np,np,2,2)                    ! metric tensor on velocity and pressure grid
 real (kind=r8)    :: metdet(np,np)                        ! g = SQRT(det(g_ij)) on velocity and pressure grid
 real (kind=r8)    :: rmetdet(np,np)                       ! 1/metdet on velocity pressure grid
 real (kind=r8)    :: D(np,np,2,2)                         ! Map covariant field on cube to vector field on the sphere
 real (kind=r8)    :: Dinv(np,np,2,2)                      ! Map vector field on the sphere to covariant v on cube


 ! Mass flux across the sides of each sub-element.
 ! The storage is redundent since the mass across shared sides
 ! must be equal in magnitude and opposite in sign.
 ! The layout is like:
 !   --------------------------------------------------------------
 ! ^|    (1,4,3)     |                |              |    (4,4,3) |
 ! ||                |                |              |            |
 ! ||(1,4,4)         |                |              |(4,4,4)     |
 ! ||         (1,4,2)|                |              |     (4,4,2)|
 ! ||                |                |              |            |
 ! ||   (1,4,1)      |                |              |  (4,4,1)   |
 ! |---------------------------------------------------------------
 ! S|                |                |              |            |
 ! e|                |                |              |            |
 ! c|                |                |              |            |
 ! o|                |                |              |            |
 ! n|                |                |              |            |
 ! d|                |                |              |            |
 !  ---------------------------------------------------------------
 ! C|                |                |              |            |
 ! o|                |                |              |            |
 ! o|                |                |              |            |
 ! r|                |                |              |            |
 ! d|                |                |              |            |
 ! i|                |                |              |            |
 ! n---------------------------------------------------------------
 ! a|    (1,1,3)     |                |              |    (4,1,3) |
 ! t|                |                |              |(4,1,4)     |
 ! e|(1,1,4)         |                |              |            |
 !  |         (1,1,2)|                |              |     (4,1,2)|
 !  |                |                |              |            |
 !  |    (1,1,1)     |                |              |  (4,1,1)   |
 !  ---------------------------------------------------------------
 !          First Coordinate ------->
 real (kind=r8) :: sub_elem_mass_flux(nc,nc,4,nlev)

 ! Convert vector fields from spherical to rectangular components
 ! The transpose of this operation is its pseudoinverse.
 real (kind=r8)    :: vec_sphere2cart(np,np,3,2)

 ! Mass matrix terms for an element on a cube face
 real (kind=r8)    :: mp(np,np)                            ! mass matrix on v and p grid
 real (kind=r8)    :: rmp(np,np)                           ! inverse mass matrix on v and p grid

 ! Mass matrix terms for an element on the sphere
 ! This mass matrix is used when solving the equations in weak form
 ! with the natural (surface area of the sphere) inner product
 real (kind=r8)    :: spheremp(np,np)                      ! mass matrix on v and p grid
 real (kind=r8)    :: rspheremp(np,np)                     ! inverse mass matrix on v and p grid

 integer(i8) :: gdofP(np,np)                     ! global degree of freedom (P-grid)

 real (kind=r8)    :: fcor(np,np)                          ! Coreolis term

 type (index_t) :: idxP
 type (index_t),pointer :: idxV
 integer :: FaceNum

 ! force element_t to be a multiple of 8 bytes.
 ! on BGP, code will crash (signal 7, or signal 15) if 8 byte alignment is off
 ! check core file for:
 ! core.63:Generated by interrupt..(Alignment Exception DEAR=0xa1ef671c ESR=0x01800000 CCR0=0x4800a002)
 integer :: dummy
end type element_t

! From cime/src/externals/pio1/pio/pio_types.F90
type, public :: var_desc_t
   
   integer(i4)     :: varID
   integer(i4)     :: rec   ! This is a record number or pointer into the unlim dimension of the
                                  ! netcdf file
   integer(i4)     :: type
   integer(i4)     :: ndims ! number of dimensions as defined on the netcdf file.
   character(len=50) :: name ! vdc needed variable
end type var_desc_t

! 
type, public :: horiz_coord_t
  private
  character(len=max_hcoordname_len) :: name = ''  ! coordinate name
  character(len=max_hcoordname_len) :: dimname = ''  ! dimension name
        ! NB: If dimname is blank, it is assumed to be name
  integer                   :: dimsize = 0       ! global size of dimension
  character(len=max_chars)  :: long_name = ''    ! 'long_name' attribute
  character(len=max_chars)  :: units = ''        ! 'units' attribute
  real(r8),         pointer :: values(:) => NULL() ! dim values (local if map)
  integer(iMap),    pointer :: map(:) => NULL()  ! map (dof) for dist. coord
  logical                   :: latitude          ! .false. means longitude
  real(r8),         pointer :: bnds(:,:) => NULL() ! bounds, if present
  type(var_desc_t), pointer :: vardesc => NULL() ! If we are to write coord
  type(var_desc_t), pointer :: bndsvdesc => NULL() ! If we are to write bounds
  contains
  procedure                 :: get_coord_len  => horiz_coord_len
  procedure                 :: num_elem       => horiz_coord_num_elem
  procedure                 :: global_size    => horiz_coord_find_size
  procedure                 :: get_coord_name => horiz_coord_name
  procedure                 :: get_dim_name   => horiz_coord_dim_name
  procedure                 :: get_long_name  => horiz_coord_long_name
  procedure                 :: get_units      => horiz_coord_units
  ! procedure                 :: write_attr     => write_horiz_coord_attr
  ! procedure                 :: write_var      => write_horiz_coord_var
end type horiz_coord_t

contains

subroutine define_cam_grids()

   ! Create grid objects on the dynamics decomposition for grids used by
   ! the dycore.  The decomposed grid object contains data for the elements
   ! in each task and information to map that data to the global grid.
   !
   ! Notes on dynamic memory management:
   !
   ! . Coordinate values and the map passed to the horiz_coord_create
   !   method are copied to the object.  The memory may be deallocated
   !   after the object is created.
   !
   ! . The area values passed to cam_grid_attribute_register are only pointed
   !   to by the attribute object, so that memory cannot be deallocated.  But the
   !   map is copied.
   !
   ! . The grid_map passed to cam_grid_register is just pointed to.
   !   Cannot be deallocated.
   
   ! Note from Ben: the horiz_coord_t and its procedures are now declared in this
   ! subroutine
   ! the horiz_coord_create function is also defined in the contains section of
   ! the subroutine.
   ! use cam_grid_support, only: horiz_coord_t, horiz_coord_create
   ! Note from Ben: cam_grid_register and cam_grid_attribute_register aren't
   ! strictly needed for this. Comment out the use statments and the function
   ! calls within the body of the subroutine.
   ! use cam_grid_support, only: cam_grid_register, cam_grid_attribute_register
   ! BKJ MPI_MAX, MPI_INTEGER and mpicom aren't actually used in this 
   ! use spmd_utils,       only: MPI_MAX, MPI_INTEGER, mpicom

   ! Local variables

   integer                      :: i, ii, j, k, ie, mapind
   character(len=8)             :: latname, lonname, ncolname, areaname

   type(horiz_coord_t), pointer :: lat_coord
   type(horiz_coord_t), pointer :: lon_coord
   integer(iMap),       pointer :: grid_map(:,:)

   real(r8),        allocatable :: pelat_deg(:)  ! pe-local latitudes (degrees)
   real(r8),        allocatable :: pelon_deg(:)  ! pe-local longitudes (degrees)
   real(r8),        pointer     :: pearea(:) => null()  ! pe-local areas
   real(r8)                     :: areaw(np,np)
   integer(iMap)                :: fdofP_local(npsq,nelemd) ! pe-local map for dynamics decomp
   integer(iMap),   allocatable :: pemap(:)                 ! pe-local map for PIO decomp

   integer                      :: ncols_fvm, ngcols_fvm
   real(r8),        allocatable :: fvm_coord(:)
   real(r8),            pointer :: fvm_area(:)
   integer(iMap),       pointer :: fvm_map(:)

   integer                      :: ncols_physgrid, ngcols_physgrid
   real(r8),        allocatable :: physgrid_coord(:)
   real(r8),            pointer :: physgrid_area(:)
   integer(iMap),       pointer :: physgrid_map(:)

   type (spherical_polar_t) :: center_cart(nc,nc)        ! center of fvm cell in gnomonic coordinates   
   type (spherical_polar_t) , allocatable :: center_cart_physgrid(:,:)        ! center of fvm cell in gnomonic         coordinates

   
   !----------------------------------------------------------------------------

   !-----------------------
   ! Create GLL grid object
   !-----------------------

   ! Calculate the mapping between element GLL points and file order
   fdofp_local = 0_iMap
   do ie = 1, nelemd
      do ii = 1, elem(ie)%idxP%NumUniquePts
         i = elem(ie)%idxP%ia(ii)
         j = elem(ie)%idxP%ja(ii)
         fdofp_local((np*(j-1))+i,ie) = elem(ie)%idxP%UniquePtoffset + ii - 1
      end do
   end do

   allocate(pelat_deg(np*np*nelemd))
   allocate(pelon_deg(np*np*nelemd))
   allocate(pearea(np*np*nelemd))
   allocate(pemap(np*np*nelemd))

   pemap = 0_iMap
   ii = 1
   do ie = 1, nelemd
      areaw = 1.0_r8 / elem(ie)%rspheremp(:,:)
      pearea(ii:ii+npsq-1) = reshape(areaw, (/ np*np /))
      pemap(ii:ii+npsq-1) = fdofp_local(:,ie)
      do j = 1, np
         do i = 1, np
            pelat_deg(ii) = elem(ie)%spherep(i,j)%lat * rad2deg
            pelon_deg(ii) = elem(ie)%spherep(i,j)%lon * rad2deg
            ii = ii + 1
         end do
      end do
   end do

   ! If using the physics grid then the GLL grid will use the names with
   ! '_d' suffixes and the physics grid will use the unadorned names.
   ! This allows fields on both the GLL and physics grids to be written to history
   ! output files.
   if (fv_nphys > 0) then
      latname  = 'lat_d'
      lonname  = 'lon_d'
      ncolname = 'ncol_d'
      areaname = 'area_d'
   else
      latname  = 'lat'
      lonname  = 'lon'
      ncolname = 'ncol'
      areaname = 'area'
   end if
   lat_coord => horiz_coord_create(trim(latname), trim(ncolname), ngcols_d,  &
         'latitude', 'degrees_north', 1, size(pelat_deg), pelat_deg, map=pemap)
   lon_coord => horiz_coord_create(trim(lonname), trim(ncolname), ngcols_d,  &
         'longitude', 'degrees_east', 1, size(pelon_deg), pelon_deg, map=pemap)

   ! Map for GLL grid
   allocate(grid_map(3,npsq*nelemd))
   grid_map = 0_iMap
   mapind = 1
   do j = 1, nelemd
      do i = 1, npsq
         grid_map(1, mapind) = i
         grid_map(2, mapind) = j
         grid_map(3, mapind) = pemap(mapind)
         mapind = mapind + 1
      end do
   end do

   ! The native SE GLL grid
   ! Note from Ben: these functions aren't needed for the kernel, so they are 
   ! commented out.
   ! call cam_grid_register('GLL', dyn_decomp, lat_coord, lon_coord,           &
   !       grid_map, block_indexed=.false., unstruct=.true.)
   ! call cam_grid_attribute_register('GLL', trim(areaname), 'gll grid areas', &
   !       trim(ncolname), pearea, map=pemap)
   ! call cam_grid_attribute_register('GLL', 'np', '', np)
   ! call cam_grid_attribute_register('GLL', 'ne', '', ne)

   ! Coordinate values and maps are copied into the coordinate and attribute objects.
   ! Locally allocated storage is no longer needed.
   deallocate(pelat_deg)
   deallocate(pelon_deg)
   deallocate(pemap)

   ! pearea cannot be deallocated as the attribute object is just pointing
   ! to that memory.  It can be nullified since the attribute object has
   ! the reference.
   nullify(pearea)

   ! grid_map cannot be deallocated as the cam_filemap_t object just points
   ! to it.  It can be nullified.
   nullify(grid_map)

   !---------------------------------
   ! Create FVM grid object for CSLAM
   !---------------------------------
   
   ! BKJ Not trying to create FVM grid yet
  !  if (ntrac > 0) then

  !     ncols_fvm = nc * nc * nelemd
  !     ngcols_fvm = nc * nc * nelem_d
  !     allocate(fvm_coord(ncols_fvm))
  !     allocate(fvm_map(ncols_fvm))
  !     allocate(fvm_area(ncols_fvm))

  !     do ie = 1, nelemd
  !        k = 1
  !        do j = 1, nc
  !           do i = 1, nc
  !              mapind = k + ((ie - 1) * nc * nc)
  !              fvm_coord(mapind) = fvm(ie)%center_cart(i,j)%lon*rad2deg
  !              fvm_map(mapind) = k + ((elem(ie)%GlobalId-1) * nc * nc)
  !              fvm_area(mapind) = fvm(ie)%area_sphere(i,j)
  !              k = k + 1
  !           end do
  !        end do
  !     end do
  !     lon_coord => horiz_coord_create('lon_fvm', 'ncol_fvm', ngcols_fvm,      &
  !          'longitude', 'degrees_east', 1, size(fvm_coord), fvm_coord,        &
  !          map=fvm_map)

  !     do ie = 1, nelemd
  !        k = 1
  !        do j = 1, nc
  !           do i = 1, nc
  !              mapind = k + ((ie - 1) * nc * nc)
  !              fvm_coord(mapind) = fvm(ie)%center_cart(i,j)%lat*rad2deg
  !              k = k + 1
  !           end do
  !        end do
  !     end do
  !     lat_coord => horiz_coord_create('lat_fvm', 'ncol_fvm', ngcols_fvm,      &
  !          'latitude', 'degrees_north', 1, size(fvm_coord), fvm_coord,        &
  !          map=fvm_map)

  !     ! Map for FVM grid
  !     allocate(grid_map(3, ncols_fvm))
  !     grid_map = 0_iMap
  !     mapind = 1
  !     do j = 1, nelemd
  !        do i = 1, nc*nc
  !           grid_map(1, mapind) = i
  !           grid_map(2, mapind) = j
  !           grid_map(3, mapind) = fvm_map(mapind)
  !           mapind = mapind + 1
  !        end do
  !     end do

  !     ! create FVM (CSLAM) grid object
  !     call cam_grid_register('FVM', fvm_decomp, lat_coord, lon_coord,         &
  !          grid_map, block_indexed=.false., unstruct=.true.)
  !     call cam_grid_attribute_register('FVM', 'area_fvm', 'fvm grid areas',   &
  !          'ncol_fvm', fvm_area, map=fvm_map)
  !     call cam_grid_attribute_register('FVM', 'nc', '', nc)
  !     call cam_grid_attribute_register('FVM', 'ne', '', ne)

  !     deallocate(fvm_coord)
  !     deallocate(fvm_map)
  !     nullify(fvm_area)
  !     nullify(grid_map)

  !  end if

   !------------------------------------------------------------------
   ! Create grid object for physics grid on the dynamics decomposition
   !------------------------------------------------------------------

   if (fv_nphys > 0) then

      ncols_physgrid = fv_nphys * fv_nphys * nelemd
      ngcols_physgrid = fv_nphys * fv_nphys * nelem_d
      allocate(physgrid_coord(ncols_physgrid))
      allocate(physgrid_map(ncols_physgrid))
      allocate(physgrid_area(ncols_physgrid))

      do ie = 1, nelemd
         k = 1
         do j = 1, fv_nphys
            do i = 1, fv_nphys
               mapind = k + ((ie - 1) * fv_nphys * fv_nphys)
               physgrid_coord(mapind) = fvm(ie)%center_cart_physgrid(i,j)%lon*rad2deg
               physgrid_map(mapind) = k + ((elem(ie)%GlobalId-1) * fv_nphys * fv_nphys)
               physgrid_area(mapind) = fvm(ie)%area_sphere_physgrid(i,j)
               k = k + 1
            end do
         end do
      end do
      lon_coord => horiz_coord_create('lon', 'ncol', ngcols_physgrid,      &
           'longitude', 'degrees_east', 1, size(physgrid_coord), physgrid_coord,   &
           map=physgrid_map)

      do ie = 1, nelemd
         k = 1
         do j = 1, fv_nphys
            do i = 1, fv_nphys
               mapind = k + ((ie - 1) * fv_nphys * fv_nphys)
               physgrid_coord(mapind) = fvm(ie)%center_cart_physgrid(i,j)%lat*rad2deg
               k = k + 1
            end do
         end do
      end do
      lat_coord => horiz_coord_create('lat', 'ncol', ngcols_physgrid,      &
           'latitude', 'degrees_north', 1, size(physgrid_coord), physgrid_coord,   &
           map=physgrid_map)

      ! Map for physics grid
      allocate(grid_map(3, ncols_physgrid))
      grid_map = 0_iMap
      mapind = 1
      do j = 1, nelemd
         do i = 1, fv_nphys*fv_nphys
            grid_map(1, mapind) = i
            grid_map(2, mapind) = j
            grid_map(3, mapind) = physgrid_map(mapind)
            mapind = mapind + 1
         end do
      end do

      ! create physics grid object
      ! call cam_grid_register('physgrid_d', physgrid_d, lat_coord, lon_coord, &
      !      grid_map, block_indexed=.false., unstruct=.true.)
      ! call cam_grid_attribute_register('physgrid_d', 'area_physgrid', 'physics grid areas',   &
      !      'ncol', physgrid_area, map=physgrid_map)
      ! call cam_grid_attribute_register('physgrid_d', 'fv_nphys', '', fv_nphys)
      ! call cam_grid_attribute_register('physgrid_d', 'ne',       '', ne)

      deallocate(physgrid_coord)
      deallocate(physgrid_map)
      nullify(physgrid_area)
      nullify(grid_map)

   end if

   nullify(lat_coord)         ! Belongs to grid
   nullify(lon_coord)         ! Belongs to grid

end subroutine define_cam_grids

!!#######################################################################
!!
!! Horizontal coordinate functions
!!
!!#######################################################################

integer function horiz_coord_find_size(this, dimname) result(dimsize)
  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  character(len=*),     intent(in)    :: dimname

  dimsize = -1
  if (len_trim(this%dimname) == 0) then
    if(trim(dimname) == trim(this%name)) then
      dimsize = this%dimsize
    end if
  else
    if(trim(dimname) == trim(this%dimname)) then
      dimsize = this%dimsize
    end if
  end if

end function horiz_coord_find_size

integer function horiz_coord_num_elem(this)
  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this

  if (associated(this%values)) then
    horiz_coord_num_elem = size(this%values)
  else
    horiz_coord_num_elem = 0
  end if

end function horiz_coord_num_elem

subroutine horiz_coord_len(this, clen)
  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  integer,              intent(out)   :: clen

  clen = this%dimsize
end subroutine horiz_coord_len

subroutine horiz_coord_name(this, name)
  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  character(len=*),     intent(out)   :: name

  if (len(name) < len_trim(this%name)) then
    call endrun('horiz_coord_name: input name too short')
  end if
  name = trim(this%name)
end subroutine horiz_coord_name

subroutine horiz_coord_dim_name(this, dimname)
  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  character(len=*),     intent(out)   :: dimname

  if (len_trim(this%dimname) > 0) then
    ! We have a separate dimension name (e.g., ncol)
    if (len(dimname) < len_trim(this%dimname)) then
      call endrun('horiz_coord_dimname: input name too short')
    end if
    dimname = trim(this%dimname)
  else
    ! No dimension name so we use the coordinate's name
    ! i.e., The dimension name is the same as the coordinate variable
    if (len(dimname) < len_trim(this%name)) then
      call endrun('horiz_coord_dimname: input name too short')
    end if
    dimname = trim(this%name)
  end if
end subroutine horiz_coord_dim_name

subroutine horiz_coord_long_name(this, name)

  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  character(len=*),     intent(out)   :: name

  if (len(name) < len_trim(this%long_name)) then
    call endrun('horiz_coord_long_name: input name too short')
  else
    name = trim(this%long_name)
  end if

end subroutine horiz_coord_long_name

subroutine horiz_coord_units(this, units)

  ! Dummy arguments
  class(horiz_coord_t), intent(in)    :: this
  character(len=*),     intent(out)   :: units

  if (len(units) < len_trim(this%units)) then
    call endrun('horiz_coord_units: input units too short')
  else
    units = trim(this%units)
  end if

end subroutine horiz_coord_units

function horiz_coord_create(name, dimname, dimsize, long_name, units,       &
     lbound, ubound, values, map, bnds) result(newcoord)

  ! Dummy arguments
  character(len=*),      intent(in)                  :: name
  character(len=*),      intent(in)                  :: dimname
  integer,               intent(in)                  :: dimsize
  character(len=*),      intent(in)                  :: long_name
  character(len=*),      intent(in)                  :: units
  ! NB: Sure, pointers would have made sense but . . . PGI
  integer,               intent(in)                  :: lbound
  integer,               intent(in)                  :: ubound
  real(r8),              intent(in)                  :: values(lbound:ubound)
  integer(iMap),         intent(in), optional        :: map(ubound-lbound+1)
  real(r8),              intent(in), optional        :: bnds(2,lbound:ubound)
  type(horiz_coord_t),               pointer         :: newcoord

  allocate(newcoord)

  newcoord%name      = trim(name)
  newcoord%dimname   = trim(dimname)
  newcoord%dimsize   = dimsize
  newcoord%long_name = trim(long_name)
  newcoord%units     = trim(units)
  ! Figure out if this is a latitude or a longitude using CF standard
  ! http://cfconventions.org/Data/cf-conventions/cf-conventions-1.6/build/cf-conventions.html#latitude-coordinate
  ! http://cfconventions.org/Data/cf-conventions/cf-conventions-1.6/build/cf-conventions.html#longitude-coordinate
  if ( (trim(units) == 'degrees_north')    .or.                             &
       (trim(units) == 'degree_north')     .or.                             &
       (trim(units) == 'degree_N')         .or.                             &
       (trim(units) == 'degrees_N')        .or.                             &
       (trim(units) == 'degreeN')          .or.                             &
       (trim(units) == 'degreesN')) then
    newcoord%latitude  = .true.
  else if ((trim(units) == 'degrees_east') .or.                             &
       (trim(units) == 'degree_east')      .or.                             &
       (trim(units) == 'degree_E')         .or.                             &
       (trim(units) == 'degrees_E')        .or.                             &
       (trim(units) == 'degreeE')          .or.                             &
       (trim(units) == 'degreesE')) then
    newcoord%latitude  = .false.
  else
    call endrun("horiz_coord_create: unsupported units: '"//trim(units)//"'")
  end if
  allocate(newcoord%values(lbound:ubound))
  if (ubound >= lbound) then
    newcoord%values(:) = values(:)
  end if

  if (present(map)) then
    if (ANY(map < 0)) then
      call endrun("horiz_coord_create "//trim(name)//": map vals < 0")
    end if
    allocate(newcoord%map(ubound - lbound + 1))
    if (ubound >= lbound) then
      newcoord%map(:) = map(:)
    end if
  else
    nullify(newcoord%map)
  end if

  if (present(bnds)) then
    allocate(newcoord%bnds(2, lbound:ubound))
    if (ubound >= lbound) then
      newcoord%bnds = bnds
    end if
  else
    nullify(newcoord%bnds)
  end if

end function horiz_coord_create

!---------------------------------------------------------------------------
!
!  write_horiz_coord_attr
!
!  Write the dimension and coordinate attributes for a horizontal grid
!  coordinate.
!
!---------------------------------------------------------------------------

! subroutine write_horiz_coord_attr(this, File, dimid_out)
!   use pio, only: file_desc_t, pio_put_att, pio_noerr, pio_double
!   use pio, only: pio_bcast_error, pio_seterrorhandling, pio_inq_varid
!   use cam_pio_utils, only: cam_pio_def_dim, cam_pio_def_var

!   ! Dummy arguments
!   class(horiz_coord_t), intent(inout) :: this
!   type(file_desc_t),    intent(inout) :: File         ! PIO file Handle
!   integer,    optional, intent(out)   :: dimid_out

!   ! Local variables
!   type(var_desc_t)                    :: vardesc
!   character(len=max_hcoordname_len)   :: dimname
!   integer                             :: dimid        ! PIO dimension ID
!   integer                             :: bnds_dimid   ! PIO dim ID for bounds
!   integer                             :: err_handling
!   integer                             :: ierr

!   ! We will handle errors for this routine
!      call pio_seterrorhandling(File, PIO_BCAST_ERROR,err_handling)

!   ! Make sure the dimension exists in the file
!   call this%get_dim_name(dimname)
!   call cam_pio_def_dim(File, trim(dimname), this%dimsize, dimid,       &
!        existOK=.true.)
!   ! Should we define the variable?
!   ierr = pio_inq_varid(File, trim(this%name), vardesc)
!   if (ierr /= PIO_NOERR) then
!     ! Variable not already defined, it is up to us to define the variable
!     if (associated(this%vardesc)) then
!       ! This should not happen (i.e., internal error)
!       call endrun('write_horiz_coord_attr: vardesc already allocated for '//trim(dimname))
!     end if
!     allocate(this%vardesc)
!     call cam_pio_def_var(File, trim(this%name), pio_double,                 &
!          (/ dimid /), this%vardesc, existOK=.false.)
!     ierr= pio_put_att(File, this%vardesc, '_FillValue', grid_fill_value)
!     call cam_pio_handle_error(ierr, 'Error writing "_FillValue" attr in write_horiz_coord_attr')
!     ! long_name
!     ierr=pio_put_att(File, this%vardesc, 'long_name', trim(this%long_name))
!     call cam_pio_handle_error(ierr, 'Error writing "long_name" attr in write_horiz_coord_attr')
!     ! units
!     ierr=pio_put_att(File, this%vardesc, 'units', trim(this%units))
!     call cam_pio_handle_error(ierr, 'Error writing "units" attr in write_horiz_coord_attr')
!     ! Take care of bounds if they exist
!     if (associated(this%bnds)) then
!       allocate(this%bndsvdesc)
!       ierr=pio_put_att(File, this%vardesc, 'bounds', trim(this%name)//'_bnds')
!       call cam_pio_handle_error(ierr, 'Error writing "'//trim(this%name)//'_bnds" attr in write_horiz_coord_attr')
!       call cam_pio_def_dim(File, 'nbnd', 2, bnds_dimid, existOK=.true.)
!       call cam_pio_def_var(File, trim(this%name)//'_bnds', pio_double,      &
!            (/ bnds_dimid, dimid /), this%bndsvdesc, existOK=.false.)
!       call cam_pio_handle_error(ierr, 'Error defining "'//trim(this%name)//'bnds" in write_horiz_coord_attr')
!       ! long_name
!       ierr=pio_put_att(File, this%bndsvdesc, 'long_name', trim(this%name)//' bounds')
!       call cam_pio_handle_error(ierr, 'Error writing bounds "long_name" attr in write_horiz_coord_attr')
!       ! fill value
!       ierr= pio_put_att(File, this%vardesc, '_FillValue', grid_fill_value)
!       call cam_pio_handle_error(ierr, 'Error writing "_FillValue" attr in write_horiz_coord_attr')
!       ! units
!       ierr=pio_put_att(File, this%bndsvdesc, 'units', trim(this%units))
!       call cam_pio_handle_error(ierr, 'Error writing bounds "units" attr in write_horiz_coord_attr')
!     end if ! There are bounds for this coordinate
!   end if ! We define the variable

!   if (present(dimid_out)) then
!     dimid_out = dimid
!   end if

!   ! Back to old error handling
!   call pio_seterrorhandling(File, err_handling)
! 
! end subroutine write_horiz_coord_attr

!---------------------------------------------------------------------------
!
!  write_horiz_coord_var
!
!  Write the coordinate values for this coordinate
!
!---------------------------------------------------------------------------

! subroutine write_horiz_coord_var(this, File)
!   use cam_pio_utils, only: cam_pio_get_decomp
!   use pio,           only: file_desc_t, pio_double, iosystem_desc_t
!   use pio,           only: pio_put_var, pio_write_darray
!   use pio,           only: pio_bcast_error, pio_seterrorhandling
!   !!XXgoldyXX: HACK to get around circular dependencies. Fix this!!
!   !!XXgoldyXX: The issue is cam_pio_utils depending on stuff in this module
!   use pio,          only: pio_initdecomp, io_desc_t, pio_freedecomp, pio_syncfile
!   use cam_instance, only: atm_id
!   use shr_pio_mod,  only: shr_pio_getiosys
!   !!XXgoldyXX: End of this part of the hack

!   ! Dummy arguments
!   class(horiz_coord_t),    intent(inout) :: this
!   type(file_desc_t),       intent(inout) :: File ! PIO file Handle

!   ! Local variables
!   character(len=120)                     :: errormsg
!   integer                                :: ierr
!   integer                                :: ldims(1)
!   integer                                :: fdims(1)
!   integer                                :: err_handling
!   type(io_desc_t)                        :: iodesc
!   !!XXgoldyXX: HACK to get around circular dependencies. Fix this!!
!   type(iosystem_desc_t), pointer         :: piosys
!   !!XXgoldyXX: End of this part of the hack

!   ! Check to make sure we are supposed to write this var
!   if (associated(this%vardesc)) then
!     ! We will handle errors for this routine
!      call pio_seterrorhandling(File, PIO_BCAST_ERROR,err_handling)

!     ! Write out the values for this dimension variable
!     if (associated(this%map)) then
!       ! This is a distributed variable, use pio_write_darray
! #if 0
!       ldims(1) = this%num_elem()
!       call this%get_coord_len(fdims(1))
!       allocate(iodesc)
!       call cam_pio_get_decomp(iodesc, ldims, fdims, PIO_DOUBLE, this%map)
!       call pio_write_darray(File, this%vardesc, iodesc, this%values, ierr)
!       nullify(iodesc) ! CAM PIO system takes over memory management of iodesc
! #else
!       !!XXgoldyXX: HACK to get around circular dependencies. Fix this!!
!       piosys => shr_pio_getiosys(atm_id)
!       call pio_initdecomp(piosys, pio_double, (/this%dimsize/), this%map,   &
!            iodesc)
!       call pio_write_darray(File, this%vardesc, iodesc, this%values, ierr)

!       call pio_syncfile(File)
!       call pio_freedecomp(File, iodesc)
!       ! Take care of bounds if they exist
!       if (associated(this%bnds) .and. associated(this%bndsvdesc)) then
!         call pio_initdecomp(piosys, pio_double, (/2, this%dimsize/),        &
!              this%map, iodesc)
!         call pio_write_darray(File, this%bndsvdesc, iodesc, this%bnds, ierr)
!         call pio_syncfile(File)
!         call pio_freedecomp(File, iodesc)
!       end if
! #endif
!       !!XXgoldyXX: End of this part of the hack
!     else
!       ! This is a local variable, pio_put_var should work fine
!       ierr = pio_put_var(File, this%vardesc, this%values)
!       ! Take care of bounds if they exist
!       if (associated(this%bnds) .and. associated(this%bndsvdesc)) then
!         ierr = pio_put_var(File, this%bndsvdesc, this%bnds)
!       end if
!     end if
!     write(errormsg, *) 'Error writing variable values for ',trim(this%name),&
!          ' in write_horiz_coord_var'
!     call cam_pio_handle_error(ierr, errormsg)

!     ! Back to old error handling
!     call pio_seterrorhandling(File, err_handling)

!     ! We are done with this variable descriptor, reset for next file
!     deallocate(this%vardesc)
!     nullify(this%vardesc)
!     ! Same with the bounds descriptor
!     if (associated(this%bndsvdesc)) then
!       deallocate(this%bndsvdesc)
!       nullify(this%bndsvdesc)
!     end if
!   end if ! Do we write the variable?

! end subroutine write_horiz_coord_var

end module grid
