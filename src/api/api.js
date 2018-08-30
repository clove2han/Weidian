
// const title = 'http://10.0.0.63:7443';
const title = 'http://120.79.182.43:7443';

const api={
  login: title + '/user/login',//用户登录
  get_all_banner: title + '/banner/get_all',//获取首页轮播图
  get_all_hotmessage: title + '/hotmessage/get_all',//获取首页热文
  get_all_activity: title + '/activity/get_all',//获取首页/发现页活动
  get_home_topnav:title + '/topnav/get_home',//获取首页导航

  get_dp_topnav: title + '//topnav/get_dp',//获取上部导航 - 发现页
  get_info_recommend: title + '/recommend/get_info',//获取每日推荐内容 - 发现页
  get_all_recommendbanner: title + '/recommendbanner/get_all',//获取上部轮播图 - 发现页
}

export default api