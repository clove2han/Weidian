# *- coding:utf8 *-
import flask_restful
from WeiDian import create_app

from WeiDian.apis.v1 import AActivity, AHotMessage, ABanner, ASearchField, ATopNav, ASuperUser, AProduct
from WeiDian.common.base_error import ApiException
from test.test_maketoken import create_test_url

wd = create_app()
api = flask_restful.Api(wd)
api.add_resource(AActivity, '/activity/<string:activity>')
api.add_resource(AHotMessage, '/hotmessage/<string:hotmessage>')
api.add_resource(ABanner, '/banner/<string:banner>')
api.add_resource(ATopNav, '/topnav/<string:topnav>')
api.add_resource(ASearchField, '/searchfield/<string:searchfield>')
api.add_resource(ASuperUser, '/super/<string:super>')
api.add_resource(AProduct, '/product/<string:product>')


# 测试
create_test_url(wd)
@wd.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    if not wd.config['DEBUG']:
        raise ApiException()
    raise e


if __name__ == '__main__':
    wd.run(debug=True)
