webpackJsonp([4],{"7owX":function(t,s){},AMDm:function(t,s,i){"use strict";var a=i("Au9i"),e={data:function(){return{name:"productQuantity",quantity:1,inputValue:1}},props:{},methods:{deductQuantity:function(){this.quantity>1&&(this.quantity-=1,console.log("数量",this.quantity))},changeQuantity:function(){Object(a.MessageBox)({$type:"prompt",title:"修改购买数量",message:" ",inputPattern:/^[0-9]/,inputErrorMessage:"数量必须为数字",showInput:!0}).then(function(t){var s=t.value;"confirm"==t.action&&console.log(s)})},addQuantity:function(){this.quantity+=1,console.log("数量",this.quantity)}},created:function(){this.inputValue=this.quantity}},c={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"product-quantity m-ft-24"},[i("div",{staticClass:"deduct-add",on:{click:t.deductQuantity}},[t._v("-")]),t._v(" "),i("div",{staticClass:"quantity",on:{click:t.changeQuantity}},[t._v(t._s(t.quantity))]),t._v(" "),i("div",{staticClass:"deduct-add",on:{click:t.addQuantity}},[t._v("+")])])},staticRenderFns:[]};var o=i("VU/8")(e,c,!1,function(t){i("7owX")},null,null);s.a=o.exports},CgRU:function(t,s,i){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var a={data:function(){return{name:"productDetail",collectionVisible:!1,ownerVisible:!0,commitmentList:["正品保障","发货&售后","七天退货","先行赔付"],evaluationTabs:["衣服不错(50)","面料好(30)","穿着舒服(30)"],evaluationPictures:["http://image2.suning.cn/content/catentries/00000000010295/000000000102956200/fullimage/000000000102956200_8f.jpg","http://image4.suning.cn/content/catentries/00000000010292/000000000102925077/fullimage/000000000102925077_6f.jpg","http://img0.imgtn.bdimg.com/it/u=12035839,3404122673&fm=26&gp=0.jpg","http://image3.suning.cn/content/catentries/00000000010295/000000000102955143/fullimage/000000000102955143_2f.jpg"],brandList:[{img:"http://pic1.win4000.com/wallpaper/8/599d1d60036a2.jpg"},{img:"http://bbsfiles.vivo.com.cn/vivobbs/attachment/forum/201804/25/145712qjc3gwcbtvgoct9w.jpg"},{img:"http://pic1.win4000.com/wallpaper/6/57eb314a3c143.jpg"},{img:"http://pic1.win4000.com/wallpaper/8/57eb322625b50.jpg"},{img:"http://pic1.win4000.com/wallpaper/6/59bcc06f60ecf.jpg"},{img:"http://pic1.win4000.com/wallpaper/6/59bcc080092c6.jpg"},{img:"http://pic1.win4000.com/wallpaper/6/59bcc07478a17.jpg"},{img:"http://pic1.win4000.com/wallpaper/6/59bcc08474821.jpg"}]}},components:{productParams:i("aJjY").a},methods:{backPage:function(){this.$router.push("/shopping/index")},collection:function(){this.collectionVisible?this.collectionVisible=!1:this.collectionVisible||(this.collectionVisible=!0)},shareProduct:function(){},getEvaluation:function(){},moreEvaluation:function(){},toService:function(){},addCart:function(){},buyNow:function(){this.$router.push({path:"/submitOrder",query:{order:""}})}},created:function(){var t=this.$route.query.prid;console.log(t)}},e={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",[i("img",{staticClass:"back-img",attrs:{src:""},on:{click:t.backPage}}),t._v(" "),i("img",{staticClass:"product-img",attrs:{src:"http://s9.rr.itc.cn/r/wapChange/20167_8_22/a87n9v8965341955628.jpg"}}),t._v(" "),t._m(0),t._v(" "),i("div",{staticClass:"product-prices"},[i("span",{staticClass:"new-price m-ft-38 m-black m-ft-b"},[t._v("￥160")]),t._v(" "),i("span",{staticClass:"old-price m-grey m-ft-28"},[t._v("￥299")]),t._v(" "),i("span",{staticClass:"make-money m-ft-38 m-red m-ft-b tl"},[t._v("赚12.5")]),t._v(" "),t.collectionVisible?i("img",{staticClass:"collection-share-img",attrs:{src:"/static/images/icon-unlike.png"},on:{click:t.collection}}):t._e(),t._v(" "),t.collectionVisible?t._e():i("img",{staticClass:"collection-share-img",attrs:{src:"/static/images/icon-like.png"},on:{click:t.collection}}),t._v(" "),i("img",{staticClass:"collection-share-img",attrs:{src:"/static/images/icon-share.png"},on:{click:t.shareProduct}})]),t._v(" "),i("div",{staticClass:"product-name m-ft-32 tl"},[t._v("【眼唇速效 卸妆神器】 Bifesta斌若诗 眼唇卸妆液  145ml 曼巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴拉巴")]),t._v(" "),i("div",{staticClass:"product-buyer-quantity m-ft-28 m-grey tl"},[t._v("20.5万人购买")]),t._v(" "),t.ownerVisible?i("div",{staticClass:"owner-price m-ft-26 m-bg-main-color"},[i("img",{staticClass:"owner-price-img",attrs:{src:"/static/images/icon-radio.png"}}),t._v(" "),i("span",{staticClass:"owner-price-one tl"},[t._v("店主价￥55.00")]),t._v(" "),i("span",{staticClass:"owner-price-two tr"},[t._v("成为店主 >")])]):t._e(),t._v(" "),t._l(t.commitmentList,function(s){return i("div",{staticClass:"product-commitment"},[i("img",{staticClass:"commitment-img",attrs:{src:"/static/images/commitment.png"}}),t._v(" "),i("div",{staticClass:"commitment-text"},[t._v(t._s(s))])])}),t._v(" "),i("product-params",{attrs:{choose:!1}}),t._v(" "),i("div",{staticClass:"rectangular"}),t._v(" "),t._m(1),t._v(" "),t._l(t.evaluationTabs,function(s){return i("div",{staticClass:"evaluation-tabs"},[i("div",{staticClass:"evaluation-tab m-ft-20",on:{click:t.getEvaluation}},[t._v(t._s(s))])])}),t._v(" "),i("div",{staticClass:"one-evaluation"},[t._m(2),t._v(" "),i("div",{staticClass:"evaluation-text m-ft-20 m-grey-color"},[t._v("一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺一级赞！很喜欢这个裤子 面料很挺")]),t._v(" "),t._l(t.evaluationPictures,function(t){return i("span",{staticClass:"evaluation-pictures"},[i("img",{staticClass:"evaluation-picture",attrs:{src:t}})])}),t._v(" "),i("div",{staticClass:"more-evaluation m-ft-20 m-grey-color",on:{click:t.moreEvaluation}},[t._v("查看更多>>")])],2),t._v(" "),t._m(3),t._v(" "),i("div",{staticClass:"product-detail-text m-ft-22 m-grey-color"},[t._v("—— 详情 ——")]),t._v(" "),i("ul",{staticStyle:{"margin-bottom":"15%"}},t._l(t.brandList,function(t){return i("li",[i("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.img,expression:"brand.img"}],staticClass:"detail-img"})])})),t._v(" "),i("div",{staticClass:"to-buy"},[i("span",{staticClass:"service-add",on:{click:t.toService}},[i("img",{staticClass:"to-buy-icon m-ft-20",attrs:{src:"/static/images/product_detail_service.png"}}),t._v(" "),i("p",{staticClass:"to-buy-text m-ft-20"},[t._v("客服")])]),t._v(" "),i("span",{staticClass:"service-add",on:{click:t.addCart}},[i("img",{staticClass:"to-buy-icon m-ft-20",attrs:{src:"/static/images/produc_detail_shopping_cart.png"}}),t._v(" "),i("p",{staticClass:"to-buy-text m-ft-20"},[t._v("购物车")])]),t._v(" "),i("span",{staticClass:"to-buy-btn m-ft-36 m-bg-main-color",on:{click:t.buyNow}},[t._v("立即购买")])])],2)},staticRenderFns:[function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"product-activity m-ft-26 m-bg-main-color"},[s("span",{staticClass:"activity-text-one"},[this._v("限时特卖")]),this._v(" "),s("span",{staticClass:"activity-text-two tr"},[this._v("距离结束仅剩")]),this._v(" "),s("span",{staticClass:"activity-text-three"},[this._v("2天07时11分28秒")])])},function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"product-evaluation"},[s("div",{staticClass:"evaluation-title m-ft-26 m-grey-color b"},[this._v("商品评价（99+）")]),this._v(" "),s("div",{staticClass:"applause-rate m-ft-26 m-grey m-ft-b tr"},[this._v("好评率99.8%")])])},function(){var t=this.$createElement,s=this._self._c||t;return s("div",{staticClass:"evaluator"},[s("img",{staticClass:"evaluator-img",attrs:{src:"http://a.hiphotos.baidu.com/zhidao/pic/item/21a4462309f79052782f28490ff3d7ca7bcbd591.jpg"}}),this._v(" "),s("div",{staticClass:"evaluator-name m-grey m-ft-20"},[this._v("欣**3")])])},function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"recommended"},[i("div",{staticClass:"recommended-title m-ft-22 m-grey-color"},[t._v("—— 配套推荐 ——")]),t._v(" "),i("div",{staticClass:"recommended-imgs"},[i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])]),t._v(" "),i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])]),t._v(" "),i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])]),t._v(" "),i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])]),t._v(" "),i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])]),t._v(" "),i("div",{staticClass:"recommended-box"},[i("img",{staticClass:"recommended-img",attrs:{src:"http://v1.51camel.com/Resources/uploadFile/L_Logo/largepic/20110509135116.jpg"}}),t._v(" "),i("p",{staticClass:"recommended-name m-ft-20 m-grey-color"},[t._v("太阳帽女防晒防")]),t._v(" "),i("p",{staticClass:"recommended-price m-ft-22 m-red"},[t._v("￥160")])])])])}]};var c=i("VU/8")(a,e,!1,function(t){i("EwXw")},"data-v-8a153148",null);s.default=c.exports},EwXw:function(t,s){},aJjY:function(t,s,i){"use strict";var a={data:function(){return{name:"productParams",popupVisible:!1,prompt:"请选择颜色、尺码",sel:[],colorSizeList:["",""],options:[{name:"颜色",items:[{id:0,msg:"黄色"},{id:1,msg:"绿色"},{id:2,msg:"红色"},{id:3,msg:"蓝色"}]},{name:"尺寸",items:[{id:0,msg:"S"},{id:1,msg:"M"},{id:2,msg:"L"},{id:3,msg:"XL"},{id:4,msg:"2XL"},{id:5,msg:"3XL"}]}]}},components:{productQuantity:i("AMDm").a},props:{choose:{type:Boolean,default:!1},size:{type:String,default:null},color:{type:String,default:null},quantity:{type:Number,default:1}},methods:{productParams:function(){if(this.popupVisible)this.popupVisible=!1;else if(!this.popupVisible){this.popupVisible=!0;for(var t=0;t<this.options.length;t++)for(var s=0;s<this.options[t].items.length;s++)this.color==this.options[t].items[s].msg&&(this.sel[0]=this.options[t].items[s].id,this.colorSizeList[0]=this.color),this.size==this.options[t].items[s].msg&&(this.sel[1]=this.options[t].items[s].id,this.colorSizeList[1]=this.size);this.changePrompt()}},select:function(t,s){this.sel[t]=s,this.sel=this.sel.concat([]),this.colorSizeList[t]=this.options[t].items[s].msg,this.changePrompt()},changePrompt:function(){if(""==this.colorSizeList[0]&&""!=this.colorSizeList[1])this.prompt="请选择 颜色";else if(""==this.colorSizeList[1]&&""!=this.colorSizeList[0])this.prompt="请选择 尺寸";else if(""!=this.colorSizeList[0]&&""!=this.colorSizeList[1]){for(var t="",s=0;s<this.colorSizeList.length;s++)t=t+" "+this.colorSizeList[s];this.prompt="已选择 "+t}},chooseDone:function(){""!=this.colorSizeList[0]&&""!=this.colorSizeList[1]&&(console.log(this.colorSizeList),this.popupVisible=!1)}},created:function(){}},e={render:function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"product-params"},[t.choose?t._e():i("div",{staticClass:"product-params-choose",on:{click:t.productParams}},[i("div",{staticClass:"product-params-text m-ft-26 m-grey tl"},[t._v("规格数量选择")]),t._v(" "),i("img",{staticClass:"more-params",attrs:{src:"/static/images/icon-list-right.png"}})]),t._v(" "),t.choose?i("div",{staticClass:"product-params-show",on:{click:t.productParams}},[i("span",{staticClass:"product-params-detail m-ft-22 m-grey"},[t._v("尺寸："+t._s(t.size))]),i("span",{staticClass:"product-params-detail"},[t._v("颜色："+t._s(t.color))]),t._v(" "),t.popupVisible?i("img",{staticClass:"list-right-down",attrs:{src:"/static/images/icon-list-down.png"}}):t._e(),t._v(" "),t.popupVisible?t._e():i("img",{staticClass:"list-right-down",attrs:{src:"/static/images/icon-list-right.png"}})]):t._e(),t._v(" "),i("mt-popup",{attrs:{position:"bottom"},model:{value:t.popupVisible,callback:function(s){t.popupVisible=s},expression:"popupVisible"}},[i("div",{staticClass:"product-params-content"},[i("img",{staticClass:"product-img",attrs:{src:"/static/images/product1.png"}}),t._v(" "),i("div",{staticClass:"product-params-center"},[i("p",{staticClass:"product-price m-ft-20 m-red m-ft-b tl"},[t._v("￥"),i("span",{staticClass:"m-ft-34"},[t._v("160")])]),t._v(" "),i("div",{staticClass:"choose-prompt m-ft-26 tl"},[t._v(t._s(t.prompt))])]),t._v(" "),i("img",{staticClass:"close-popup",attrs:{src:"/static/images/delete.png"},on:{click:t.productParams}})]),t._v(" "),i("div",{staticClass:"line"}),t._v(" "),t._l(t.options,function(s,a){return i("div",{staticClass:"product-size-color"},[i("p",{staticClass:"product-size-color-text m-ft-30 tl"},[t._v(t._s(s.name))]),t._v(" "),t._l(s.items,function(s,e){return i("span",{class:{select:t.sel[a]==e},on:{click:function(s){t.select(a,e)}}},[t._v(t._s(s.msg))])})],2)}),t._v(" "),i("div",{staticClass:"line"}),t._v(" "),i("div",{staticClass:"product-quantity"},[i("div",{staticClass:"product-quantity-text m-ft-30 tl"},[t._v("购买数量")]),t._v(" "),i("product-quantity",{staticClass:"product-quantity-edit",attrs:{quantity:t.quantity}})],1),t._v(" "),i("div",{staticClass:"choose-done m-ft-28 m-bg-main-color",on:{click:t.chooseDone}},[t._v("确定")])],2)],1)},staticRenderFns:[]};var c=i("VU/8")(a,e,!1,function(t){i("rvdT")},null,null);s.a=c.exports},rvdT:function(t,s){}});
//# sourceMappingURL=4.116abf29feef718e89dc.js.map