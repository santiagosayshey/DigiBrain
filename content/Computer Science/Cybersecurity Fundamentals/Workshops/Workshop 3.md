
> [!exercise]+ What is (are) the IP addresses for the FQDN (fully qualified domain name) www.netflix.com?

```
;; ANSWER SECTION:
www.netflix.com.        300     IN      CNAME   www.dradis.netflix.com.
www.dradis.netflix.com. 60      IN      CNAME   www.us-west-2.internal.dradis.netflix.com.
www.us-west-2.internal.dradis.netflix.com. 60 IN CNAME apiproxy-website-nlb-prod-1-bcf28d21f4bbcf2c.elb.us-west-2.amazonaws.com.

;; AUTHORITY SECTION:
elb.us-west-2.amazonaws.com. 60 IN      SOA     ns-1870.awsdns-41.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 60
```


> [!exercise]+ Where do emails sent to @student.adelaide.edu.au get routed to?
> 

```
dig MX student.adelaide.edu.au

;; ANSWER SECTION:
student.adelaide.edu.au. 300    IN      MX      10 au-smtp-inbound-2.mimecast.com.
student.adelaide.edu.au. 300    IN      MX      10 au-smtp-inbound-1.mimecast.com.
```