// Generated by gencpp from file ld_actions/GoToResult.msg
// DO NOT EDIT!


#ifndef LD_ACTIONS_MESSAGE_GOTORESULT_H
#define LD_ACTIONS_MESSAGE_GOTORESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ld_actions
{
template <class ContainerAllocator>
struct GoToResult_
{
  typedef GoToResult_<ContainerAllocator> Type;

  GoToResult_()
    : status()  {
    }
  GoToResult_(const ContainerAllocator& _alloc)
    : status(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _status_type;
  _status_type status;





  typedef boost::shared_ptr< ::ld_actions::GoToResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ld_actions::GoToResult_<ContainerAllocator> const> ConstPtr;

}; // struct GoToResult_

typedef ::ld_actions::GoToResult_<std::allocator<void> > GoToResult;

typedef boost::shared_ptr< ::ld_actions::GoToResult > GoToResultPtr;
typedef boost::shared_ptr< ::ld_actions::GoToResult const> GoToResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ld_actions::GoToResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ld_actions::GoToResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ld_actions

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'ld_actions': ['/home/tthmatt/ld_ROS/devel/.private/ld_actions/share/ld_actions/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ld_actions::GoToResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ld_actions::GoToResult_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ld_actions::GoToResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ld_actions::GoToResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ld_actions::GoToResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ld_actions::GoToResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ld_actions::GoToResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4fe5af303955c287688e7347e9b00278";
  }

  static const char* value(const ::ld_actions::GoToResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4fe5af303955c287ULL;
  static const uint64_t static_value2 = 0x688e7347e9b00278ULL;
};

template<class ContainerAllocator>
struct DataType< ::ld_actions::GoToResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ld_actions/GoToResult";
  }

  static const char* value(const ::ld_actions::GoToResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ld_actions::GoToResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Result\n"
"string status\n"
"\n"
;
  }

  static const char* value(const ::ld_actions::GoToResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ld_actions::GoToResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GoToResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ld_actions::GoToResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ld_actions::GoToResult_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.status);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LD_ACTIONS_MESSAGE_GOTORESULT_H
