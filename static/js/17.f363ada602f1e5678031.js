webpackJsonp([17],{XHF0:function(t,a){},mZs9:function(t,a,s){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var i=s("C3lA"),e=s("zpT/"),c={name:"memberDetail",data:function(){return{nav_list:[{click:!0,tnname:"全部(158人)"},{click:!1,tnname:"已开单(68人)"},{click:!1,tnname:"未开单(90人)"}],trList:[{src:"/static/images/product1.png",name:"xxx",order:{quantity:"200",reduce:!0},forwarding:{quantity:"200",reduce:!0},people:{quantity:"200",reduce:!0}},{src:"/static/images/product1.png",name:"xxx",order:{quantity:"200",reduce:!0},forwarding:{quantity:"200",reduce:!0},people:{quantity:"200",reduce:!0}},{src:"/static/images/product1.png",name:"xxx",order:{quantity:"200",reduce:!0},forwarding:{quantity:"200",reduce:!0},people:{quantity:"200",reduce:!0}}]}},components:{navbar:i.a,differentDays:e.a},methods:{navClick:function(t){console.log(t);for(var a=this.nav_list,s=0;s<a.length;s++)a[s].click=!1;a[t].click=!0,this.nav_list=[].concat(a)}}},n={render:function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",[s("navbar",{attrs:{list:t.nav_list},on:{navClick:t.navClick}}),t._v(" "),t._m(0),t._v(" "),s("different-days"),t._v(" "),s("div",{staticClass:"detail-table"},[t._m(1),t._v(" "),t._l(t.trList,function(a,i){return s("div",{staticClass:"detail-table-row"},[s("img",{staticClass:"tr-img",attrs:{src:a.src}}),t._v(" "),s("div",{staticClass:"tr-name",class:0==i?"active":""},[t._v(t._s(a.name))]),t._v(" "),s("div",{staticClass:"detail-tr"},[s("span",{staticClass:"detail-tr-num",class:0==i?"active":""},[t._v("20")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_down.png"}})]),t._v(" "),s("div",{staticClass:"detail-tr"},[s("span",{staticClass:"detail-tr-num",class:0==i?"active":""},[t._v("500")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_up.png"}})]),t._v(" "),s("div",{staticClass:"detail-tr"},[s("span",{staticClass:"detail-tr-num",class:0==i?"active":""},[t._v("6")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_up.png"}})])])})],2)],1)},staticRenderFns:[function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"detail-prompt"},[a("p",{staticClass:"detail-prompt-text"},[this._v("今日提示：")]),this._v(" "),a("p",{staticClass:"detail-prompt-text"},[this._v("你今日需要培训56人，分别是金金、小婷。。。。。")]),this._v(" "),a("p",{staticClass:"detail-prompt-text"},[this._v("等姓名颜色标红者。")]),this._v(" "),a("p",{staticClass:"detail-prompt-text"},[this._v("理由：累计订单超过20笔，持续上升幅度较高。")])])},function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"detail-table-header"},[s("div",{staticClass:"detail-th detail-th-text"},[t._v("微信名")]),t._v(" "),s("div",{staticClass:"detail-th"},[s("span",{staticClass:"detail-th-text"},[t._v("订单量")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_up.png"}}),t._v(" "),s("span",{staticClass:"detail-th-num m-red"},[t._v("3%")])]),t._v(" "),s("div",{staticClass:"detail-th"},[s("span",{staticClass:"detail-th-text"},[t._v("转发量")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_up.png"}}),t._v(" "),s("span",{staticClass:"detail-th-num m-red"},[t._v("3%")])]),t._v(" "),s("div",{staticClass:"detail-th"},[s("span",{staticClass:"detail-th-text"},[t._v("直收人数")]),t._v(" "),s("img",{staticClass:"growth-reduce-img",attrs:{src:"/static/images/num_down.png"}}),t._v(" "),s("span",{staticClass:"detail-th-num m-blue"},[t._v("3%")])])])}]};var r=s("VU/8")(c,n,!1,function(t){s("XHF0")},null,null);a.default=r.exports}});
//# sourceMappingURL=17.f363ada602f1e5678031.js.map