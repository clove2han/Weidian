webpackJsonp([16],{"+b97":function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=s("Au9i"),i=s("7+uW"),r=s("mtWM"),d=s.n(r),o=s("P9l9"),n=s("QLTB"),c=s("CaOM");i.default.component(a.Picker.name,a.Picker);var m={data:function(){return{radio_select:!0,form:{UAdefault:!1,UAname:"",UAphone:"",UAtext:"",UAid:""},show_picker:!1,address_id:{provinceid:"",cityid:"",areaid:""},address:{province:"",city:"",area:""},address_list:{province:[],city:[],area:[]},slots:[{flex:1,values:["浙江","上海","重庆","四川","安徽"],className:"slot1",textAlign:"center"}],params:"province"}},components:{picker:n.a},methods:{getSlot:function(e){var t=this;switch(e){case"province":d.a.get(o.a.get_province).then(function(s){200==s.data.status&&(t.address_list[e]=s.data.data,t.slots[0].values=t.dealArr(s.data.data))});break;case"city":d.a.get(o.a.get_city,{params:{provinceid:this.address_id.provinceid}}).then(function(s){200==s.data.status&&(t.address_list[e]=s.data.data,t.slots[0].values=t.dealArr(s.data.data))});break;case"area":d.a.get(o.a.get_area,{params:{cityid:this.address_id.cityid}}).then(function(s){200==s.data.status&&(t.address_list[e]=s.data.data,t.slots[0].values=t.dealArr(s.data.data))})}},radioChange:function(){this.form.UAdefault=!this.form.UAdefault},pickerSave:function(e,t,s){if(e||(this.show_picker=e),"province"==s?this.show_picker=e:"city"==s?this.address_id.provinceid?this.show_picker=e:Object(a.Toast)("请依次选择省-市-区/县"):"area"==s&&(this.address_id.provinceid&&this.address_id.cityid?this.show_picker=e:Object(a.Toast)("请依次选择省-市-区/县")),t){this.address[s]=t;for(var i=0;i<this.address_list[s].length;i++)this.address_list[s][i].name==t&&(this.address_id[s+"id"]=this.address_list[s][i][s+"id"])}else""==t&&s&&this.show_picker&&(this.params=s,this.getSlot(s))},saveClick:function(){var e=this;this.form.UAdefault=Boolean(this.form.UAdefault),this.form.areaid=this.address_id.areaid,this.form.UAname&&""!=this.form.UAphone&&this.form.UAtext&&this.form.areaid?this.form.UAid?d.a.post(o.a.update_address+"?token="+localStorage.getItem("token")+"&uaid="+this.form.UAid,this.form).then(function(t){200==t.data.status?(Object(a.Toast)({message:"修改成功",className:"m-toast-success"}),e.$router.push("/receiverAddress")):Object(a.Toast)({message:t.data.message,className:"m-toast-warning"})}):d.a.post(o.a.add_address+"?token="+localStorage.getItem("token"),this.form).then(function(t){200==t.data.status?(Object(a.Toast)({message:"添加成功",className:"m-toast-success"}),e.$router.push("/receiverAddress")):Object(a.Toast)({message:t.data.message,className:"m-toast-warning"})}):(Object(a.Toast)("请完整填写收货地址"),console.log(this.form.UAdefault,this.form.UAname,""!=this.form.UAphone,this.form.UAtext,this.form.areaid))},delClick:function(){var e=this;d.a.post(o.a.del_address+"?token="+localStorage.getItem("token"),{UAid:this.form.UAid}).then(function(t){200==t.data.status?(Object(a.Toast)({message:"删除成功",className:"m-toast-success"}),e.$router.push("/receiverAddress")):Object(a.Toast)({message:t.data.message,className:"m-toast-warning"})})},dealArr:function(e){for(var t=[],s=0;s<e.length;s++)t.push(e[s].name);return t}},mounted:function(){this.$route.query&&(this.form.UAdefault=this.$route.query.UAdefault,this.form.UAname=this.$route.query.UAname,this.form.UAphone=this.$route.query.UAphone,this.form.UAtext=this.$route.query.UAtext,this.form.UAid=this.$route.query.UAid,this.address.province=this.$route.query.province,this.address.city=this.$route.query.city,this.address.area=this.$route.query.area,this.address_id.provinceid=this.$route.query.provinceid,this.address_id.cityid=this.$route.query.cityid,this.address_id.areaid=this.$route.query.areaid),c.a.changeTitle("编辑地址")},created:function(){}},l={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"m-editAddress"},[s("div",{staticClass:"m-editAddress-form"},[s("div",{staticClass:"m-editAddress-row"},[s("span",{staticClass:"m-editAddress-row-name"},[e._v("收货人")]),e._v(" "),s("div",[s("div",{staticClass:"m-editAddress-input-box"},[s("input",{directives:[{name:"model",rawName:"v-model",value:e.form.UAname,expression:"form.UAname"}],staticClass:"m-editAddress-input",attrs:{type:"text",placeholder:"输入收货人姓名"},domProps:{value:e.form.UAname},on:{input:function(t){t.target.composing||e.$set(e.form,"UAname",t.target.value)}}})]),e._v(" "),s("div",{staticClass:"m-editAddress-input-box"},[s("input",{directives:[{name:"model",rawName:"v-model",value:e.form.UAphone,expression:"form.UAphone"}],staticClass:"m-editAddress-input",attrs:{type:"number",placeholder:"输入收货人联系方式"},domProps:{value:e.form.UAphone},on:{input:function(t){t.target.composing||e.$set(e.form,"UAphone",t.target.value)}}})])])]),e._v(" "),s("div",{staticClass:"m-editAddress-row"},[s("span",{staticClass:"m-editAddress-row-name"},[e._v("收货地址")]),e._v(" "),s("div",[s("div",{staticClass:"m-editAddress-input-box"},[s("input",{directives:[{name:"model",rawName:"v-model",value:e.address.province,expression:"address.province"}],staticClass:"m-editAddress-input m-s",attrs:{type:"text",placeholder:"选择省",readonly:""},domProps:{value:e.address.province},on:{click:function(t){e.pickerSave(!0,"","province")},input:function(t){t.target.composing||e.$set(e.address,"province",t.target.value)}}}),e._v(" "),s("span",[e._v("-")]),e._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:e.address.city,expression:"address.city"}],staticClass:"m-editAddress-input m-s",attrs:{type:"text",placeholder:"选择市",readonly:""},domProps:{value:e.address.city},on:{click:function(t){e.pickerSave(!0,"","city")},input:function(t){t.target.composing||e.$set(e.address,"city",t.target.value)}}}),e._v(" "),s("span",[e._v("-")]),e._v(" "),s("input",{directives:[{name:"model",rawName:"v-model",value:e.address.area,expression:"address.area"}],staticClass:"m-editAddress-input m-s",attrs:{type:"text",placeholder:"选择区(县)",readonly:""},domProps:{value:e.address.area},on:{click:function(t){e.pickerSave(!0,"","area")},input:function(t){t.target.composing||e.$set(e.address,"area",t.target.value)}}})]),e._v(" "),s("div",{staticClass:"m-editAddress-input-box"},[s("input",{directives:[{name:"model",rawName:"v-model",value:e.form.UAtext,expression:"form.UAtext"}],staticClass:"m-editAddress-input",attrs:{type:"text",placeholder:"输入详情街道地址"},domProps:{value:e.form.UAtext},on:{input:function(t){t.target.composing||e.$set(e.form,"UAtext",t.target.value)}}})])])])]),e._v(" "),s("div",{staticClass:"m-editAddress-switch"},[s("span",[e._v("设为默认")]),e._v(" "),s("span",{staticClass:"m-radio",class:e.form.UAdefault?"active":"",on:{click:e.radioChange}})]),e._v(" "),e.form.UAid?s("div",{staticClass:"m-editAddress-switch",on:{click:e.delClick}},[s("span",{staticClass:"m-red"},[e._v("删除收货地址")])]):e._e(),e._v(" "),s("div",{staticClass:"m-address-btn",on:{click:e.saveClick}},[e._v("保存")]),e._v(" "),s("picker",{attrs:{slots:e.slots,params:e.params,show_picker:e.show_picker},on:{pickerSave:e.pickerSave}})],1)},staticRenderFns:[]};var u=s("VU/8")(m,l,!1,function(e){s("RHq9")},"data-v-bbc3048a",null);t.default=u.exports},RHq9:function(e,t){}});
//# sourceMappingURL=16.e2ab80cf5ff8a4243acf.js.map