#! /usr/bin/guile
!#

;this is my first guile program

(define (f x)
 (if (< x 10) (+ x 12) (- x 12)))

(define (faci x)
 (if (zero? x) 1 (* x (faci (- x 1))) ))

(begin (display "hello the world!")
	(newline)
	(display (f 8))
	(newline)
	(display (f 28))
	(newline)
	(display (faci 10))
	(newline))

