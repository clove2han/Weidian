webpackJsonp([41],{0:function(n,e){},"2f45":function(n,e){},"508A":function(n,e){},"5LIk":function(n,e){},"6V+c":function(n,e){},CaOM:function(n,e,t){"use strict";var o={changeTitle:function(n){document.getElementsByTagName("title")[0].innerHTML=n,window.setDocumentTitle=function(n){var e=document.createElement("iframe");e.src="../favicon.ico",e.style.display="none",e.onload=function(){setTimeout(function(){e.remove()},9)},document.body.appendChild(e)}},GetQueryString:function(n){var e=new RegExp("(^|&)"+n+"=([^&]*)(&|$)"),t=window.location.search.substr(1).match(e);return null!=t&&unescape(t[2])},getScrollTop:function(){var n=0;return document.documentElement&&document.documentElement.scrollTop?n=document.documentElement.scrollTop:document.body&&(n=document.body.scrollTop),n},getClientHeight:function(){return document.body.clientHeight&&document.documentElement.clientHeight?Math.min(document.body.clientHeight,document.documentElement.clientHeight):Math.max(document.body.clientHeight,document.documentElement.clientHeight)},getScrollHeight:function(){return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight)}};e.a=o},NHnr:function(n,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=t("//Fk"),i=t.n(o),r=t("7+uW"),c={render:function(){var n=this.$createElement,e=this._self._c||n;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var a=t("VU/8")({name:"App"},c,!1,function(n){t("508A")},null,null).exports,u=t("mtWM"),l=t.n(u),d=(t("sVYa"),t("Au9i")),s=t.n(d),h=(t("d8/S"),t("wvfG")),p=t.n(h),m=t("/ocq"),f={render:function(){var n=this.$createElement,e=this._self._c||n;return e("div",{staticClass:"hello"},[e("mt-header",{attrs:{title:this.$store.state.tabbar_select}},[e("router-link",{attrs:{slot:"left",to:"/"},slot:"left"},[e("mt-button",{attrs:{icon:"back"}})],1),this._v(" "),e("mt-button",{attrs:{slot:"right",icon:"more"},slot:"right"})],1)],1)},staticRenderFns:[]};var b=t("VU/8")({data:function(){return{}}},f,!1,function(n){t("6V+c")},"data-v-1ad62e02",null).exports,v=t("SKcX"),g={render:function(){var n=this.$createElement,e=this._self._c||n;return e("div",{staticClass:"m-content"},[e("keep-alive",[e("router-view")],1)],1)},staticRenderFns:[]};var x=t("VU/8")({data:function(){return{name:""}},components:{},methods:{},created:function(){}},g,!1,function(n){t("2f45")},"data-v-5ffb41fe",null).exports,_={data:function(){return{name:""}},components:{"m-header":b,mFooter:v.a,mContent:x},methods:{},created:function(){}},P={render:function(){var n=this.$createElement,e=this._self._c||n;return e("div",[e("m-content"),this._v(" "),e("m-footer")],1)},staticRenderFns:[]};var C=t("VU/8")(_,P,!1,function(n){t("Zh26")},"data-v-77bac65f",null).exports;r.default.use(m.a);var w=[{path:"/login",component:function(){return Promise.all([t.e(0),t.e(1)]).then(t.bind(null,"W2Q3"))},hidden:!0},{path:"/register",component:function(){return t.e(38).then(t.bind(null,"12H5"))},hidden:!0},{path:"/search",component:function(){return t.e(8).then(t.bind(null,"TRIl"))},hidden:!0},{path:"/product",component:function(){return t.e(33).then(t.bind(null,"zrP8"))},hidden:!0},{path:"/",component:C,redirect:"login",children:[{path:"/login",component:function(){return Promise.all([t.e(0),t.e(1)]).then(t.bind(null,"W2Q3"))},hidden:!0}]},{path:"/index",component:C,redirect:"index/index",children:[{path:"index",component:function(){return Promise.all([t.e(0),t.e(4)]).then(t.bind(null,"JXTs"))},name:"index",meta:{title:"index",icon:"index",noCache:!0}}]},{path:"/discover",component:C,redirect:"discover/index",children:[{path:"index",component:function(){return Promise.all([t.e(0),t.e(7)]).then(t.bind(null,"/M0C"))},name:"index",meta:{title:"index",icon:"index",noCache:!0}}]},{path:"/service",component:C,redirect:"service/index",children:[{path:"index",component:function(){return t.e(22).then(t.bind(null,"JpB7"))},name:"service",meta:{title:"service",icon:"service",noCache:!0}}]},{path:"/shopping",component:C,redirect:"shopping/index",children:[{path:"index",component:function(){return t.e(5).then(t.bind(null,"HQIK"))},name:"shopping",meta:{title:"shopping",icon:"shopping",noCache:!0}}]},{path:"/personal",component:C,redirect:"personal/index",children:[{path:"index",component:function(){return Promise.all([t.e(0),t.e(2)]).then(t.bind(null,"uTKz"))},name:"personal",meta:{title:"personal",icon:"personal",noCache:!0}}]},{path:"/setUp",component:function(){return Promise.all([t.e(0),t.e(37)]).then(t.bind(null,"C3cB"))},hidden:!0},{path:"/bankCard",component:function(){return Promise.all([t.e(0),t.e(30)]).then(t.bind(null,"WeHN"))},hidden:!0},{path:"/editAddress",component:function(){return Promise.all([t.e(0),t.e(15)]).then(t.bind(null,"+b97"))},hidden:!0},{path:"/addBankCard",component:function(){return Promise.all([t.e(0),t.e(35)]).then(t.bind(null,"lrnN"))},hidden:!0},{path:"/receiverAddress",component:function(){return Promise.all([t.e(0),t.e(17)]).then(t.bind(null,"5zbm"))},hidden:!0},{path:"/result",component:function(){return t.e(16).then(t.bind(null,"8anw"))},hidden:!0},{path:"/inviteFans",component:function(){return t.e(20).then(t.bind(null,"ctS4"))},hidden:!0},{path:"/fansManagement",component:function(){return t.e(25).then(t.bind(null,"7bjL"))},hidden:!0},{path:"/poster",component:function(){return t.e(32).then(t.bind(null,"u9if"))},hidden:!0},{path:"/inviteStore",component:function(){return Promise.all([t.e(0),t.e(3)]).then(t.bind(null,"mKah"))},hidden:!0},{path:"/invitationLetter",component:function(){return t.e(34).then(t.bind(null,"raL5"))},hidden:!0},{path:"/details",component:function(){return Promise.all([t.e(0),t.e(9)]).then(t.bind(null,"kWux"))},hidden:!0},{path:"/applyWithdrawal",component:function(){return t.e(19).then(t.bind(null,"u0Ox"))},hidden:!0},{path:"/withdrawalDetail",component:function(){return t.e(31).then(t.bind(null,"OnKA"))},hidden:!0},{path:"/order",component:function(){return Promise.all([t.e(0),t.e(10)]).then(t.bind(null,"uAJB"))},hidden:!0},{path:"/complain",component:function(){return Promise.all([t.e(0),t.e(11)]).then(t.bind(null,"VW8M"))},hidden:!0},{path:"/collect",component:function(){return Promise.all([t.e(0),t.e(29)]).then(t.bind(null,"grur"))},hidden:!0},{path:"/productDetail",component:function(){return Promise.all([t.e(0),t.e(6)]).then(t.bind(null,"CgRU"))},hidden:!0},{path:"/submitOrder",component:function(){return t.e(13).then(t.bind(null,"oUV/"))},hidden:!0},{path:"/orderPayOK",component:function(){return t.e(21).then(t.bind(null,"mbxE"))},hidden:!0},{path:"/orderStatus",component:function(){return t.e(12).then(t.bind(null,"ZV8C"))},hidden:!0},{path:"/logisticsInfo",component:function(){return t.e(27).then(t.bind(null,"+0zp"))},hidden:!0},{path:"/returnProduct",component:function(){return t.e(24).then(t.bind(null,"gJEc"))},hidden:!0},{path:"/memberCenter",component:function(){return Promise.all([t.e(0),t.e(18)]).then(t.bind(null,"fwMA"))},hidden:!0},{path:"/memberDetail",component:function(){return Promise.all([t.e(0),t.e(39)]).then(t.bind(null,"mZs9"))},hidden:!0},{path:"/resultSituation",component:function(){return Promise.all([t.e(0),t.e(26)]).then(t.bind(null,"g0gy"))},hidden:!0},{path:"/upToSpeed",component:function(){return Promise.all([t.e(0),t.e(28)]).then(t.bind(null,"6vFi"))},hidden:!0},{path:"/advancedClass",component:function(){return Promise.all([t.e(0),t.e(14)]).then(t.bind(null,"wKdF"))},hidden:!0},{path:"/helpCenter",component:function(){return Promise.all([t.e(0),t.e(36)]).then(t.bind(null,"h374"))},hidden:!0},{path:"/activityContent",component:function(){return Promise.all([t.e(0),t.e(23)]).then(t.bind(null,"/GXu"))},hidden:!0}],y=new m.a({scrollBehavior:function(){return{y:0}},routes:w}),k=t("iqGf"),$=t.n(k),T=t("v5o6"),E=t.n(T),H=t("hKoQ"),S=t.n(H),M=(t("fxnj"),t("NYxO"));r.default.use(M.a);var A=new M.a.Store({state:{route:null,now:null,token:"",tabbar:[{name:"首页",icon:"",active_icon:"",url:"index"},{name:"客服",icon:"",active_icon:"",url:"service"},{name:"发现",icon:"",active_icon:"",url:"discover"},{name:"购物车",icon:"",active_icon:"",url:"shopping"},{name:"我的",icon:"",active_icon:"",url:"personal"}],tabbar_select:"首页"},mutations:{add:function(n,e){n.tabbar_select=e},remove:function(n,e){r.default.delete(n.route,e)}}});r.default.config.productionTip=!1,r.default.use(s.a),p.a.config.autoSetContainer=!0,r.default.use(p.a),t("g3Gj"),t("5LIk"),r.default.use($.a),E.a.attach(document.body),S.a.polyfill(),r.default.prototype.$http=l.a,l.a.defaults.timeout=6e5,l.a.interceptors.request.use(function(n){return d.Indicator.open({text:"加载中...",spinnerType:"fading-circle"}),n},function(n){return d.Indicator.close(),i.a.reject(n)}),l.a.interceptors.response.use(function(n){return d.Indicator.close(),n},function(n){return d.Indicator.close(),i.a.reject(n)}),new r.default({el:"#app",router:y,store:A,components:{App:a},template:"<App/>"})},SKcX:function(n,e,t){"use strict";var o=t("CaOM"),i={data:function(){return{name:"",selected:this.$store.state.tabbar_select,tabbar:this.$store.state.tabbar}},components:{},methods:{tabbarClick:function(n){}},mounted:function(){},computed:{select:function(){return this.$store.state.tabbar_select}},watch:{selected:function(n,e){switch(this.$store.state.tabbar_select=n,o.a.changeTitle(n),n){case"首页":this.$router.push("/index");break;case"客服":this.$router.push("/service");break;case"发现":"/discover/index"==this.$route.path||this.$router.push("/discover");break;case"购物车":this.$router.push("/shopping");break;case"我的":this.$router.push("/personal")}},select:function(n){console.log("asdasda"),this.selected=this.$store.state.tabbar_select}},created:function(){}},r={render:function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("mt-tabbar",{attrs:{fixed:!0},model:{value:n.selected,callback:function(e){n.selected=e},expression:"selected"}},[n._l(n.tabbar,function(e,o){return[t("mt-tab-item",{attrs:{id:e.name},on:{click:function(t){n.tabbarClick(e)}}},[e.name==n.selected?t("img",{attrs:{slot:"icon",src:e.active_icon},slot:"icon"}):t("img",{attrs:{slot:"icon",src:e.icon},slot:"icon"}),n._v("\n      "+n._s(e.name)+"\n    ")])]})],2)},staticRenderFns:[]};var c=t("VU/8")(i,r,!1,function(n){t("pKqT")},"data-v-64b5c8e5",null);e.a=c.exports},Zh26:function(n,e){},"d8/S":function(n,e){},g3Gj:function(n,e){},pKqT:function(n,e){}},["NHnr"]);
//# sourceMappingURL=app.8afb4280573ac5c101c1.js.map