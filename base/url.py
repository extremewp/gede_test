class Url:
    def url(self, ip, url, sign):
        app_id = '10000001'
        a = url.split('?')[0]
        transaction_type = a.split('/')[-1]
        url_sign = ip + url + '?' + 'app_id=' + app_id + '&' + 'transaction_type=' + transaction_type + '&' + 'sign=' + sign
        return url_sign
