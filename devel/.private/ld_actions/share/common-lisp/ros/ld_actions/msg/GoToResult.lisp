; Auto-generated. Do not edit!


(cl:in-package ld_actions-msg)


;//! \htmlinclude GoToResult.msg.html

(cl:defclass <GoToResult> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:string
    :initform ""))
)

(cl:defclass GoToResult (<GoToResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GoToResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GoToResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ld_actions-msg:<GoToResult> is deprecated: use ld_actions-msg:GoToResult instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <GoToResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ld_actions-msg:status-val is deprecated.  Use ld_actions-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GoToResult>) ostream)
  "Serializes a message object of type '<GoToResult>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'status))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'status))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GoToResult>) istream)
  "Deserializes a message object of type '<GoToResult>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'status) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GoToResult>)))
  "Returns string type for a message object of type '<GoToResult>"
  "ld_actions/GoToResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GoToResult)))
  "Returns string type for a message object of type 'GoToResult"
  "ld_actions/GoToResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GoToResult>)))
  "Returns md5sum for a message object of type '<GoToResult>"
  "4fe5af303955c287688e7347e9b00278")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GoToResult)))
  "Returns md5sum for a message object of type 'GoToResult"
  "4fe5af303955c287688e7347e9b00278")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GoToResult>)))
  "Returns full string definition for message of type '<GoToResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%string status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GoToResult)))
  "Returns full string definition for message of type 'GoToResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%string status~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GoToResult>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GoToResult>))
  "Converts a ROS message object to a list"
  (cl:list 'GoToResult
    (cl:cons ':status (status msg))
))
