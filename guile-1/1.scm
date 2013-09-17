#! /usr/bin/guile
!#

;this is my first guile program

(define (f x)
 (if (< x 10) (+ x 12) (- x 12)))


(begin (display "hello the world!")
	(newline)
	(display (f 8))
	(newline)
	(display (f 28))
	(newline))


