webpackJsonp([37],{C3cB:function(a,s,t){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var e=t("mtWM"),n=t.n(e),r=t("P9l9"),i=t("CaOM"),o={data:function(){return{form:{usheader:"",usname:"",usphone:"",wxnum:"",bankcard:"",address:""},isOpen:!1}},components:{},mounted:function(){i.a.changeTitle("账号设置"),"partner"==localStorage.getItem("level")&&(this.isOpen=!0)},methods:{getInfo:function(){var a=this;n.a.get(r.a.get_account_info,{params:{token:localStorage.getItem("token")}}).then(function(s){200==s.data.status&&(a.form.usheader=s.data.data.user.usheader,a.form.usname=s.data.data.user.usname,a.form.usphone=s.data.data.user.usphone,a.form.wxnum=s.data.data.user.wxnum,a.form.address=s.data.data.address,a.form.bankcard=s.data.data.bankcard)})},addressClick:function(){this.$router.push("/receiverAddress")},addChange:function(){this.$router.push("/addBankCard")},barkChange:function(){this.$router.push("/bankCard")}},created:function(){this.getInfo()}},c={render:function(){var a=this,s=a.$createElement,t=a._self._c||s;return t("div",{staticClass:"m-setUp"},[t("div",{staticClass:"m-setUp-logo"},[t("img",{staticClass:"m-logo",attrs:{src:a.form.usheader,alt:""}})]),a._v(" "),t("div",{staticClass:"m-setUp-form"},[t("div",{staticClass:"m-row"},[t("span",{staticClass:"m-form-label"},[a._v("昵称")]),a._v(" "),t("span",{staticClass:"m-setUp-input"},[a._v(a._s(a.form.usname))])]),a._v(" "),t("div",{staticClass:"m-row"},[t("span",{staticClass:"m-form-label"},[a._v("手机号")]),a._v(" "),t("span",{staticClass:"m-setUp-input"},[a._v(a._s(a.form.usphone))])]),a._v(" "),t("div",{staticClass:"m-row"},[t("span",{staticClass:"m-form-label"},[a._v("地址")]),a._v(" "),t("span",{staticClass:"m-setUp-input"},[a._v(a._s(a.form.address))]),a._v(" "),t("span",{staticClass:"m-row-btn",on:{click:a.addressClick}},[a._v("编辑")])]),a._v(" "),a.isOpen?t("div",{staticClass:"m-row"},[t("span",{staticClass:"m-form-label"},[a._v("银行卡")]),a._v(" "),t("span",{staticClass:"m-setUp-input"},[a._v(a._s(a.form.bankcard))]),a._v(" "),a.form.bankcard?t("span",{staticClass:"m-row-btn",on:{click:a.barkChange}},[a._v("更换")]):t("span",{staticClass:"m-row-btn",on:{click:a.addChange}},[a._v("绑定")])]):a._e()]),a._v(" "),a._m(0)])},staticRenderFns:[function(){var a=this.$createElement,s=this._self._c||a;return s("div",{staticClass:"m-setUp-btn"},[s("span",[this._v("退出登录")])])}]};var d=t("VU/8")(o,c,!1,function(a){t("IXHB")},"data-v-1c5b5f3d",null);s.default=d.exports},IXHB:function(a,s){}});
//# sourceMappingURL=37.bce93d1368a6ef59297a.js.map