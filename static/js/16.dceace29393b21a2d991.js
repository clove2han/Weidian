webpackJsonp([16],{mbxE:function(t,n,e){"use strict";Object.defineProperty(n,"__esModule",{value:!0});var a={data:function(){return{name:"orderPayOK",order:{}}},methods:{shareImg:function(){var t=["https://daaiti.cn/static/clothesdemo0919120348.png","https://daaiti.cn/static/clothesdemo0919120348.png","/static/images/share/product2.png","/static/images/share/product4.png","/static/images/share/product5.png","/static/images/share/product.jpg"],n=document.createElement("canvas"),e=n.getContext("2d");n.height=1275,4==t.length?n.width=1525:6==t.length&&(n.width=2150),e.rect(0,0,n.width,n.height),e.fillStyle="#fff",e.fill(),e.fillStyle="#000000",e.font="30px PingFang-SC";for(var a="商品标题商品标题商品标题商品标题商品标题商品标题商品标题商品标题商品标题商",r=0;r<12;r++)e.fillText(a[r],90+34*r,970);for(var o=12;o<23;o++)e.fillText(a[o],90+34*(o-12),1015),22==o&&e.fillText("...",90+34*(o-12+1),1015);e.fillStyle="#f43b51",e.font="bold 30px PingFang-SC",e.fillText("￥",90,1150),e.font="bold 58px PingFang-SC",e.fillText("129",120,1150),e.font="bold 30px PingFang-SC",e.fillText(". 50",230,1150),e.fillStyle="#a4a4a4",e.font="30px PingFang-SC",e.fillText("原价：￥298.50",90,1200);var i=new Image;i.crossOrigin="Anonymous",i.src="/static/images/share/bg_test.png",i.onload=function(){var a=new Image;a.crossOrigin="Anonymous",a.src="/static/images/share/sweep.png",a.onload=function(){e.drawImage(a,560,1190,260,60);var r=new Image;r.crossOrigin="Anonymous",r.src="/static/images/share/Qrcode.png",r.onload=function(){e.drawImage(r,560,920,260,260);var a=new Image;a.crossOrigin="Anonymous",a.src="/static/images/share/commitment.png",a.onload=function(){e.drawImage(a,50,825,800,55);var r=new Image;r.crossOrigin="Anonymous",r.src=t[0],r.onload=function(){e.drawImage(r,50,25,800,800);var a=new Image;a.crossOrigin="Anonymous",a.src=t[1],a.onload=function(){e.drawImage(a,875,25,600,600);var r=new Image;r.crossOrigin="Anonymous",r.src=t[2],r.onload=function(){e.drawImage(r,875,650,600,600);var a=new Image;a.crossOrigin="Anonymous",a.src="/static/images/share/delete.png",a.onload=function(){if(e.drawImage(a,175,1180,150,20),6==t.length){var r=new Image;r.crossOrigin="Anonymous",r.src=t[3],r.onload=function(){e.drawImage(r,1500,25,600,600);var a=new Image;a.crossOrigin="Anonymous",a.src=t[4],a.onload=function(){e.drawImage(a,1500,650,600,600);var t=n.toDataURL("image/png");document.getElementById("avatar").setAttribute("src",t)}}}if(4==t.length){var o=n.toDataURL("image/png"),i=document.getElementById("avatar");i.style.width="244px",i.style.height="204px",i.setAttribute("src",o)}}}}}}}}}},orderDetail:function(){var t=this.order;this.$router.push({path:"/orderStatus",query:{order:t}})},returnHome:function(){this.$router.push("/index")}},mounted:function(){},created:function(){this.order=this.$route.query.order}},r={render:function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",[e("div",{staticClass:"m-btn"},[e("div",{staticClass:"m-btn-text m-ft-28 m-grey-color",on:{click:function(n){t.shareImg()}}},[t._v("查看订单")])]),t._v(" "),e("img",{staticStyle:{width:"344px",height:"204px"},attrs:{id:"avatar",src:"",alt:""}}),t._v(" "),e("canvas",{attrs:{id:"myCanvas"}},[t._v("\n    Your browser does not support the HTML5 canvas tag.\n  ")])])},staticRenderFns:[]};var o=e("VU/8")(a,r,!1,function(t){e("x9A4")},"data-v-f7e1d0ac",null);n.default=o.exports},x9A4:function(t,n){}});
//# sourceMappingURL=16.dceace29393b21a2d991.js.map