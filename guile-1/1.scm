#! /usr/bin/guile -s
!#

;this is my first guile program

(define (f x)
  (if (< x 10) (+ x 12) (- x 12)))

(define (faci x)
  (if (zero? x) 1 (* x (faci (- x 1))) ))

(define company "Eddysun")
(display company)
(newline)
(set! company "ABB")
(display company)
(newline)

;procedure call
(display (string-length (string-append "kevin" " love " "lingjian")))

(newline)

;my procedure
(define myfun
  (lambda (name addr) 
	 (string-append "I love " name " live in " addr) )
  )
(display (myfun "lj" "xiamen"))

;my second procedure
(define (mynewfun name addr)
  (string-append "I love " name " live in " addr) 
  )
 
(newline)
(display (mynewfun "veer" "putian"))

(newline)

(do ((i 0 (+ 1 i)))
 ((> i 4))
 (display (mynewfun "fuck" "samming"))
 (newline)
 )

(do ((j 0 (+ 1 j)))
  ((> j 5))
  (display "happy")
  (newline)
  )

(if #T
  ((newline)
  (display "holy shit")
  (newline))
 )



(begin (display "hello the world!")
       (newline)
       (display (f 8))
       (newline)
       (display (f 28))
       (newline)
       (display (faci 10))
       (newline))
