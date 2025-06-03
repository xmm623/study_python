# HTTP相关
# 无状态性：意味着服务器不会保留关于先前请求的任何信息，每个请求都被视为独立的事务。
"""
状态码
1XX 信息性状态码，表示请求已接收，继续处理，在接口测试中少见，一般用于大文件分块上传等特殊场景。
2XX 成功状态码，200请求成功，201请求成功并且服务器创建了新资源，，通常是post或put请求成功的响应，202服务器已接受请求，但尚未处理完成，204请求成功但响应体中没有内容，通常用于delete请求成功的响应。
3XX 重定向状态码，301请求的资源已被永久移动到新URL，302请求的资源临时移动到新URL，304资源未被修改，客户端可以使用缓存的版本。
4XX 客户端错误码，400服务器无法理解客户端的请求，通常是请求语法或参数错误，401请求要求身份验证，客户端需要提供有效凭证，403服务器拒绝请求，客户端没有权限访问资源，404请求的资源不存在，405请求方法不被允许，406请求的资源无法满足客户端的条件，408请求超时，服务器在等待客户端发送请求时超时。
5XX 服务器错误码，500服务器内部错误，502网关错误，如上游服务器故障，503服务器当前无法处理请求，通常是由于过载或正在进行维护，504网关超时，服务器在等待上游服务器响应时超时。
"""

"""
请求头信息
user-agent：客户端信息
Accept：客户端可接受的内容类型
Authorization：客户端身份验证信息
Content-Type：请求体的内容类型，通常是application/json或application/x-www-form-urlencoded
Accept-Encoding：客户端可接受的内容编码方式，通常是gzip或deflate
Cookie：客户端发送的cookie信息
"""

"""
响应头信息
Content-Type：响应体的内容类型，通常是application/json或text/html
Content-Length：响应体的长度
Cache-Control：缓存控制指令，指示客户端如何缓存响应
Set-Cookie：服务器设置的cookie信息
"""

# 请求体：发送给服务端的数据，get和delete通常没有请求体，post和put请求通常包含请求体，用户创建或更新资源，请求体的格式由Content-Type头部指定，常见的格式有application/json、application/x-www-form-urlencoded和multipart/form-data。
# 响应体：服务器返回给客户端的数据，通常包含请求的结果或错误信息，响应体的格式由Content-Type头部指定，常见的格式有application/json、text/html和application/xml。