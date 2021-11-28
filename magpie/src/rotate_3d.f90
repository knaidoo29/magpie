include "math.f90"


subroutine rotmat_x(dphi, rotx)

  ! Rotation matrix for counterclockwise rotation around the x-axis.
  !
  ! Parameters
  ! ----------
  ! dphi : float
  !   Counter-clockwise rotation.
  !
  ! Returns
  ! -------
  ! rotx : array
  !   Rotation matrix around the x-axis.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: dphi
  real(kind=dp), intent(out) :: rotx(9)

  ! Main

  rotx(1) = 1.
  rotx(2) = 0.
  rotx(3) = 0.

  rotx(4) = 0.
  rotx(5) = cos(dphi)
  rotx(6) = -sin(dphi)

  rotx(7) = 0.
  rotx(8) = sin(dphi)
  rotx(9) = cos(dphi)

end subroutine rotmat_x


subroutine rotmat_y(dphi, roty)

  ! Rotation matrix for counterclockwise rotation around the y-axis.
  !
  ! Parameters
  ! ----------
  ! dphi : float
  !   Counter-clockwise rotation.
  !
  ! Returns
  ! -------
  ! roty : array
  !   Rotation matrix around the y-axis.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: dphi
  real(kind=dp), intent(out) :: roty(9)

  ! Main

  roty(1) = cos(dphi)
  roty(2) = 0.
  roty(3) = sin(dphi)

  roty(4) = 0.
  roty(5) = 1.
  roty(6) = 0.

  roty(7) = -sin(dphi)
  roty(8) = 0.
  roty(9) = cos(dphi)

end subroutine rotmat_y


subroutine rotmat_z(dphi, rotz)

  ! Rotation matrix for counterclockwise rotation around the z-axis.
  !
  ! Parameters
  ! ----------
  ! dphi : float
  !   Counter-clockwise rotation.
  !
  ! Returns
  ! -------
  ! rotz : array
  !   Rotation matrix around the z-axis.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: dphi
  real(kind=dp), intent(out) :: rotz(9)

  ! Main

  rotz(1) = cos(dphi)
  rotz(2) = -sin(dphi)
  rotz(3) = 0.

  rotz(4) = sin(dphi)
  rotz(5) = cos(dphi)
  rotz(6) = 0.

  rotz(7) = 0.
  rotz(8) = 0.
  rotz(9) = 1.

end subroutine rotmat_z


subroutine rotmat_axis(angle, axis, rot)

  ! Determines the rotation matrix from a specified axis.
  !
  ! Parameters
  ! ----------
  ! angle : float
  !   Angle of rotation around a given axis.
  ! axis : int
  !   Integer of the axis of rotation, where 0=>x-axis, 1=>y-axis, 2=>z-axis.
  !
  ! Returns
  ! -------
  ! rot : array
  !   Rotation matrix.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: angle
  integer, intent(in) :: axis
  real(kind=dp), intent(out) :: rot(9)

  ! Main

  if (axis .eq. 0) then
    call rotmat_x(angle, rot)
  else if (axis .eq. 1) then
    call rotmat_y(angle, rot)
  else
    call rotmat_z(angle, rot)
  end if

end subroutine rotmat_axis


subroutine rotmat_euler(angles, axes, rot)

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
  real(kind=dp), intent(in) :: angles(3)
  integer, intent(in) :: axes(3)
  real(kind=dp), intent(out) :: rot(9)
  real(kind=dp) :: rot1(9), rot2(9), rot3(9), rot32(9)

  ! Main

  call rotmat_axis(angles(3), axes(3), rot3)
  call rotmat_axis(angles(2), axes(2), rot2)
  call rotmat_axis(angles(1), axes(1), rot1)
  call dot3by3(rot3, rot2, rot32)
  call dot3by3(rot32, rot1, rot)

end subroutine rotmat_euler


subroutine rotmat_rodrigues(k, dphi, rot)

  ! Parameters
  ! ----------
  ! k : array
  !   k is a unit vector k around which points will be rotated by an angle
  !   dphi.
  ! dphi : float
  !   Rodrigues rotation angle around the unit vector k.
  !
  ! Returns
  ! -------
  ! rot : array
  !   Rotation matrix.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: k(3), dphi
  real(kind=dp), intent(out) :: rot(9)
  real(kind=dp) :: kmat(9)

  kmat(1) = 0.
  kmat(2) = -k(3)
  kmat(3) = k(2)

  kmat(4) = k(3)
  kmat(5) = 0.
  kmat(6) = -k(1)

  kmat(7) = -k(2)
  kmat(8) = k(1)
  kmat(9) = 0.

  rot(1) = 1. + sin(dphi)*kmat(1) + (1. - cos(dphi))*kmat(1)**2.
  rot(2) = sin(dphi)*kmat(2) + (1. - cos(dphi))*kmat(2)**2.
  rot(3) = sin(dphi)*kmat(3) + (1. - cos(dphi))*kmat(3)**2.

  rot(4) = sin(dphi)*kmat(4) + (1. - cos(dphi))*kmat(4)**2.
  rot(5) = 1. + sin(dphi)*kmat(5) + (1. - cos(dphi))*kmat(5)**2.
  rot(6) = sin(dphi)*kmat(6) + (1. - cos(dphi))*kmat(6)**2.

  rot(7) = sin(dphi)*kmat(7) + (1. - cos(dphi))*kmat(7)**2.
  rot(8) = sin(dphi)*kmat(8) + (1. - cos(dphi))*kmat(8)**2.
  rot(9) = 1. + sin(dphi)*kmat(9) + (1. - cos(dphi))*kmat(9)**2.

end subroutine rotmat_rodrigues


subroutine rotate_3d_scalar(x, y, z, rot, xrot, yrot, zrot)

  ! Rotates a single point in 3D cartesian coordinates by a rotation matrix.
  !
  ! Parameters
  ! ----------
  ! x, y, z : float
  !   Cartesian coordinates.
  ! rot : float
  !   Rotation matrix.
  !
  ! Returns
  ! -------
  ! xrot, yrot, zrot : float
  !   Rotated x, y and z coordinates.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  real(kind=dp), intent(in) :: x, y, z, rot(9)
  real(kind=dp), intent(out) :: xrot, yrot, zrot

  ! Main

  xrot = rot(1)*x + rot(2)*y + rot(3)*z
  yrot = rot(4)*x + rot(5)*y + rot(6)*z
  zrot = rot(7)*x + rot(8)*y + rot(9)*z

end subroutine rotate_3d_scalar


subroutine rotate_3d_array(x, y, z, rot, xlen, xrot, yrot, zrot)

  ! Rotates an array of points in 3D cartesian coordinates by a rotation
  ! matrix.
  !
  ! Parameters
  ! ----------
  ! x, y, z : array
  !   Cartesian coordinates.
  ! rot : float
  !   Rotation matrix.
  !
  ! Returns
  ! -------
  ! xrot, yrot, zrot : array
  !   Rotated x, y and z coordinates.

  implicit none

  ! Parameter declarations

  integer, parameter :: dp = kind(1.d0)
  integer, intent(in) :: xlen
  real(kind=dp), intent(in) :: x(xlen), y(xlen), z(xlen), rot(9)
  real(kind=dp), intent(out) :: xrot(xlen), yrot(xlen), zrot(xlen)

  integer :: i

  ! Main

  do i=1, xlen

    call rotate_3d_scalar(x(i), y(i), z(i), rot, xrot(i), yrot(i), zrot(i))

  end do

end subroutine rotate_3d_array
