webpackJsonp([30],{WeHN:function(a,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=e("mtWM"),n=e.n(s),o=e("P9l9"),c=e("Au9i"),i=e("CaOM"),d={data:function(){return{bank_info:{bcaddress:"",bcbankname:"",bcid:"",bcnumber:"",bcusername:""},show_modal:!1,code_box:["","","","","",""],count:0,isDel:!0,tel:""}},components:{},mounted:function(){this.getInfo(),i.a.changeTitle("银行卡")},methods:{getInfo:function(){var a=this;n.a.get(o.a.get_mybankcard,{params:{token:localStorage.getItem("token")}}).then(function(t){200==t.data.status?a.bank_info=t.data.data:Object(c.Toast)({message:t.data.message,className:"m-toast-fail"})},function(a){Object(c.Toast)({message:a.data.message,className:"m-toast-fail"})})},sendCode:function(){var a=this;n.a.post(o.a.get_inforcode+"?token="+localStorage.getItem("token")).then(function(t){if(200!=t.data.status)return Object(c.Toast)({message:t.data.message,className:"m-toast-fail"}),!1;Object(c.Toast)({message:t.data.message,className:"m-toast-success"}),a.tel=t.data.usphone}),this.timer||(this.count=60,this.timer=setInterval(function(){a.count>0&&a.count<=60?a.count--:(a.show=!0,clearInterval(a.timer),a.timer=null)},1e3))},changeModal:function(a,t){this.show_modal=a,a||(this.code_box=["","","","","",""]),0!==t&&1!==t||(this.isDel=Boolean(t),this.sendCode())},inputChange:function(a){if(""!=this.code_box[a]){if(5==a)return!1;var t=document.getElementById(a+1);t.focus(),t.select()}},updateCard:function(a){var t=this;if(this.code_box.join("").length<6)return!1;n.a.post(o.a.verify_inforcode+"?token="+localStorage.getItem("token"),{ICcode:this.code_box.join("")}).then(function(e){200==e.data.status?a?n.a.post(o.a.del_bankcard+"?token="+localStorage.getItem("token"),{BCid:t.bank_info.bcid}).then(function(a){Object(c.Toast)({message:a.data.message,className:"m-toast-success"}),t.$router.push({path:"/setUp",query:t.bank_info})}):t.$router.push({path:"/addBankCard",query:t.bank_info}):Object(c.Toast)({message:e.data.message,className:"m-toast-fail"})},function(a){Object(c.Toast)({message:a.data.message,className:"m-toast-fail"})})}},created:function(){}},l={render:function(){var a=this,t=a.$createElement,e=a._self._c||t;return e("div",{staticClass:"m-bankCard"},[e("div",{staticClass:"m-bankCard-box"},[e("div",{staticClass:"m-one-card"},[e("div",{staticClass:"m-bankCard-name"},[a._v(a._s(a.bank_info.bcbankname))]),a._v(" "),e("div",{staticClass:"m-bankCard-type"},[a._v("储蓄卡")]),a._v(" "),e("div",{staticClass:"m-bankCard-num"},[a._v("******* ***** ***** ***"+a._s(a.bank_info.bcnumber.substring(a.bank_info.bcnumber.length-3)))]),a._v(" "),e("span",{staticClass:"m-bankCard-cancel",on:{click:function(t){a.changeModal(!0,0)}}},[a._v("修改")])])]),a._v(" "),e("div",{staticClass:"m-bank-btn"},[e("span",{on:{click:function(t){a.changeModal(!0,1)}}},[a._v("解除绑定")])]),a._v(" "),a.show_modal?e("div",{staticClass:"m-modal "},[e("div",{staticClass:"m-modal-state m-bank-modal-state"},[e("div",{staticClass:"m-modal-head m-bank"},[e("p",[a._v("输入验证码")]),a._v(" "),e("span",{staticClass:"m-close",on:{click:function(t){a.changeModal(!1)}}},[a._v(" x ")])]),a._v(" "),e("div",{staticClass:"m-modal-content m-bank-modal"},[e("div",{staticClass:"m-bank-tel"},[e("span",[a._v(a._s(a.tel))]),a._v(" "),a.count>0?e("span",{staticClass:"m-bank-time"},[a._v(a._s(a.count)+"秒")]):e("span",{staticClass:"m-bank-time",on:{click:a.sendCode}},[a._v("重发")])]),a._v(" "),e("ul",{staticClass:"m-bank-input-box"},[a._l(a.code_box,function(t,s){return[e("li",[e("input",{directives:[{name:"model",rawName:"v-model",value:a.code_box[s],expression:"code_box[i]"}],attrs:{type:"number",id:s,oninput:"if(value.length>1)value=value.slice(0,1)"},domProps:{value:a.code_box[s]},on:{keyup:function(t){a.inputChange(s)},input:function(t){t.target.composing||a.$set(a.code_box,s,t.target.value)}}})])]})],2),a._v(" "),e("div",{staticClass:"m-bank-modal-btn"},[a.isDel?e("span",{on:{click:function(t){a.updateCard(!0)}}},[a._v("解除银行卡")]):e("span",{on:{click:function(t){a.updateCard(!1)}}},[a._v("修改银行卡")])])])])]):a._e()])},staticRenderFns:[]};var m=e("VU/8")(d,l,!1,function(a){e("uXrf")},"data-v-4704db9b",null);t.default=m.exports},uXrf:function(a,t){}});
//# sourceMappingURL=30.69e032e68c994e208e7a.js.map