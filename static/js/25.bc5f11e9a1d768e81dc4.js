webpackJsonp([25],{"5zbm":function(a,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var t=s("mtWM"),d=s.n(t),i=s("P9l9"),r={data:function(){return{have_address:!0,address_list:[],area:{province:"",city:"",area:""}}},components:{},mounted:function(){this.getInfo()},methods:{addressClick:function(a,e){e?this.$router.push({path:"/editAddress",query:{UAdefault:e.uadefault,UAname:e.uaname,UAphone:e.uaphone,UAtext:e.uatext,UAid:e.uaid,province:e.area.province,city:e.area.city,area:e.area.area,provinceid:e.area.provinceid,cityid:e.area.cityid,areaid:e.area.areaid}}):this.$router.push("/editAddress")},getInfo:function(){var a=this;d.a.get(i.a.get_address,{params:{token:localStorage.getItem("token")}}).then(function(e){if(200==e.data.status){for(var s=[],t=[],d=0;d<e.data.data.length;d++)e.data.data[d].area={province:"",city:"",area:""},e.data.data[d].uadefault?s.push(e.data.data[d]):t.push(e.data.data[d]);s=s.concat(t);for(var i=0;i<s.length;i++)s[i].area.province=s[i].addressinfo[2].name,s[i].area.area=s[i].addressinfo[0].name,s[i].area.city=s[i].addressinfo[1].name,s[i].area.provinceid=s[i].addressinfo[2].provinceid,s[i].area.areaid=s[i].addressinfo[0].areaid,s[i].area.cityid=s[i].addressinfo[1].cityid;a.address_list=[].concat(s)}})}},created:function(){}},n={render:function(){var a=this,e=a.$createElement,s=a._self._c||e;return s("div",{staticClass:"m-receiverAddress"},[a.address_list.length>0?s("div",[a._l(a.address_list,function(e,t){return[s("div",{staticClass:"m-one-address"},[s("span",{staticClass:"m-check-icon",class:e.uadefault?"active":""}),a._v(" "),s("div",{staticClass:"m-address-info"},[s("div",{staticClass:"m-address-row m-address-row1 "},[s("span",[a._v(a._s(e.uaname))]),a._v(" "),s("span",[a._v(a._s(e.uaphone))])]),a._v(" "),s("div",{staticClass:"m-address-row"},[s("div",{staticClass:"tl m-address"},[e.uadefault?s("span",{staticClass:"m-mo"},[a._v("[ 默认地址 ]")]):a._e(),a._v(" "),s("span",[a._v(a._s(e.area.province)+a._s(e.area.city)+a._s(e.area.area)+a._s(e.uatext))])]),a._v(" "),s("span",{staticClass:"m-edit",on:{click:function(s){a.addressClick(s,e)}}},[a._v("编辑")])])])])]})],2):s("div",{staticClass:"m-no-address"},[s("img",{staticClass:"m-no-address-img",attrs:{src:"/static/images/icon-no-address.png",alt:""}}),a._v(" "),s("p",[a._v("您还没有收货地址哦")])]),a._v(" "),s("div",{staticClass:"m-address-btn",on:{click:a.addressClick}},[a._v("添加新地址")])])},staticRenderFns:[]};var c=s("VU/8")(r,n,!1,function(a){s("wa2G")},null,null);e.default=c.exports},wa2G:function(a,e){}});
//# sourceMappingURL=25.bc5f11e9a1d768e81dc4.js.map