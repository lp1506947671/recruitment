#CA颁发证书的机构的RSA私钥
openssl genrsa -out ca.key 2048

#CA颁发证书的机构的RSA公钥(根证书)
openssl req -new -x509 -key ca.key -out ca.crt -days 365

#网站的私钥
openssl genrsa -out recruitment.key 2048
#网站的公钥(Certificate Signing Request)CSR包括了你的网站的公钥，以及你网站相关的信息。
openssl req -new -key recruitment.key -out recruitment.csr
# 查看CSR文件信息
openssl req -text -noout -verify -in my-website.csr

# ca对csr文件进行签名
openssl x509 -req -in recruitment.csr -CA ./ca.crt -CAkey ./ca.key -set_serial 01 -out recruitment.crt -days 365

#查看证书
openssl x509 -text -noout  -in recruitment.crt
