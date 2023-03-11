
program main
    implicit none

    double precision :: pi = 3.1415927410125732
    real :: r
    real :: c
    real :: d
    real*16 :: n

    print *, "=== Happy Pi Day ==="
    print *, "Here is some stuff you can calculate using Pi!"
    print *, "Some numbers may be wrong, as Fortran rounds the up (lol)"
    print *, "(Press any key to start)"
    read(*,*);

    print *, "Value of Pi:"
    print *, pi

    print *, "Radius of the circle :"
    read(*,*) r

    c = 2 * pi * r

    print *, "Circumference :"
    print *, c

    print *, "Diameter :"
    read(*,*) d

    n = c / d

    print *, "Pi :"
    print *, n

    print *, "=== Variable dump (end of exec.) ==="
    print *, pi, r, c, d, n

end program main
