// Generated by gencpp from file om_aiv_util/Service5Response.msg
// DO NOT EDIT!


#ifndef OM_AIV_UTIL_MESSAGE_SERVICE5RESPONSE_H
#define OM_AIV_UTIL_MESSAGE_SERVICE5RESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace om_aiv_util
{
template <class ContainerAllocator>
struct Service5Response_
{
  typedef Service5Response_<ContainerAllocator> Type;

  Service5Response_()
    : device()  {
    }
  Service5Response_(const ContainerAllocator& _alloc)
    : device(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _device_type;
  _device_type device;





  typedef boost::shared_ptr< ::om_aiv_util::Service5Response_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::om_aiv_util::Service5Response_<ContainerAllocator> const> ConstPtr;

}; // struct Service5Response_

typedef ::om_aiv_util::Service5Response_<std::allocator<void> > Service5Response;

typedef boost::shared_ptr< ::om_aiv_util::Service5Response > Service5ResponsePtr;
typedef boost::shared_ptr< ::om_aiv_util::Service5Response const> Service5ResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::om_aiv_util::Service5Response_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::om_aiv_util::Service5Response_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace om_aiv_util

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'om_aiv_util': ['/home/tthmatt/ld_ROS/src/om_aiv_util/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::om_aiv_util::Service5Response_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::om_aiv_util::Service5Response_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::om_aiv_util::Service5Response_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::om_aiv_util::Service5Response_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::om_aiv_util::Service5Response_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::om_aiv_util::Service5Response_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::om_aiv_util::Service5Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "25b143d1069c7861320973824c82b9d8";
  }

  static const char* value(const ::om_aiv_util::Service5Response_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x25b143d1069c7861ULL;
  static const uint64_t static_value2 = 0x320973824c82b9d8ULL;
};

template<class ContainerAllocator>
struct DataType< ::om_aiv_util::Service5Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "om_aiv_util/Service5Response";
  }

  static const char* value(const ::om_aiv_util::Service5Response_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::om_aiv_util::Service5Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string device\n"
"\n"
;
  }

  static const char* value(const ::om_aiv_util::Service5Response_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::om_aiv_util::Service5Response_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.device);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Service5Response_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::om_aiv_util::Service5Response_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::om_aiv_util::Service5Response_<ContainerAllocator>& v)
  {
    s << indent << "device: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.device);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OM_AIV_UTIL_MESSAGE_SERVICE5RESPONSE_H
