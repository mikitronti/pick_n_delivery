
(cl:in-package :asdf)

(defsystem "pick_n_delivery-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "NewGoal" :depends-on ("_package_NewGoal"))
    (:file "_package_NewGoal" :depends-on ("_package"))
  ))