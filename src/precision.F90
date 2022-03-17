module precision
   implicit none
   !-----------------------------------------------------------------
   ! Define precision constants for consistency across modules
   !-----------------------------------------------------------------
   
   integer, public, parameter :: r8 = selected_real_kind(12) ! 8 byte real
   integer, public, parameter :: r4 = selected_real_kind(6)  ! 4 byte real
   integer, public, parameter :: i8 = selected_int_kind(13)  ! 8 byte integer
   integer, public, parameter :: i4 = selected_int_kind(6)   ! 4 byte integer

end module precision
