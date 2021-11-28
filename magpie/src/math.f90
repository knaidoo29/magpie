
subroutine dot3by3(a, b, c)

  ! Determines the rotation matrix from the Euler angles.
  !
  ! Parameters
  ! ----------
  ! angles : array
  !   Euler angles.
  ! axes : array
  !   Integer array of axes of rotation, where 0=>x-axis, 1=>y-axis, 2=>z-axis.
  !
  ! Returns
  ! -------
  ! rot : array
  !   Rotation matrix.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: a(9), b(9)
  real(kind=dp), intent(out) :: c(9)

  ! Main

  c(1) = a(1)*b(1) + a(2)*b(4) + a(3)*b(7)
  c(2) = a(1)*b(2) + a(2)*b(5) + a(3)*b(8)
  c(3) = a(1)*b(3) + a(2)*b(6) + a(3)*b(9)

  c(4) = a(4)*b(1) + a(5)*b(4) + a(6)*b(7)
  c(5) = a(4)*b(2) + a(5)*b(5) + a(6)*b(8)
  c(6) = a(4)*b(3) + a(5)*b(6) + a(6)*b(9)

  c(7) = a(7)*b(1) + a(8)*b(4) + a(9)*b(7)
  c(8) = a(7)*b(2) + a(8)*b(5) + a(9)*b(8)
  c(9) = a(7)*b(3) + a(8)*b(6) + a(9)*b(9)

end subroutine dot3by3
