# 短信验证码有效期, 秒
SMS_VERIFICATION_CODE_EXPIRES = 5 * 60

# 根据手机号限制短信验证码发送频次
LIMIT_SMS_VERIFICATION_CODE_BY_MOBILE = '1/minute'

# 根据IP限制短信验证码发送频次
LIMIT_SMS_VERIFICATION_CODE_BY_IP = '100/hour'