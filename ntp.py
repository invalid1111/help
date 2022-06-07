import ntplib
import time
NIST = 'uk.pool.ntp.org'
ntp = ntplib.NTPClient()
ntpResponse = ntp.request(NIST)
if (ntpResponse):
    now = time.time()
    diff =ntpResponse.tx_time - now
print(diff)
