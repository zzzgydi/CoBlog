(function(e){function t(t){for(var o,i,c=t[0],s=t[1],u=t[2],l=0,f=[];l<c.length;l++)i=c[l],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&f.push(a[i][0]),a[i]=0;for(o in s)Object.prototype.hasOwnProperty.call(s,o)&&(e[o]=s[o]);d&&d(t);while(f.length)f.shift()();return r.push.apply(r,u||[]),n()}function n(){for(var e,t=0;t<r.length;t++){for(var n=r[t],o=!0,i=1;i<n.length;i++){var c=n[i];0!==a[c]&&(o=!1)}o&&(r.splice(t--,1),e=s(s.s=n[0]))}return e}var o={},i={app:0},a={app:0},r=[];function c(e){return s.p+"static/js/"+({}[e]||e)+"."+{"chunk-06792728":"4dea6419","chunk-6440f6d0":"3dadad78","chunk-3fc1a6d2":"54f33239","chunk-701d3066":"efabd855","chunk-833d1566":"87b3f874","chunk-8504c7dc":"61716c63","chunk-caeb7a62":"2bf67129","chunk-d9eafcd6":"4e47bad2"}[e]+".js"}function s(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(e){var t=[],n={"chunk-06792728":1,"chunk-6440f6d0":1,"chunk-3fc1a6d2":1,"chunk-701d3066":1,"chunk-833d1566":1,"chunk-8504c7dc":1,"chunk-caeb7a62":1,"chunk-d9eafcd6":1};i[e]?t.push(i[e]):0!==i[e]&&n[e]&&t.push(i[e]=new Promise(function(t,n){for(var o="static/css/"+({}[e]||e)+"."+{"chunk-06792728":"a922b7d4","chunk-6440f6d0":"b35fc6d0","chunk-3fc1a6d2":"e2ff9c78","chunk-701d3066":"27a9daec","chunk-833d1566":"3da742a2","chunk-8504c7dc":"29cd63b1","chunk-caeb7a62":"553a50b1","chunk-d9eafcd6":"66736cef"}[e]+".css",a=s.p+o,r=document.getElementsByTagName("link"),c=0;c<r.length;c++){var u=r[c],l=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(l===o||l===a))return t()}var f=document.getElementsByTagName("style");for(c=0;c<f.length;c++){u=f[c],l=u.getAttribute("data-href");if(l===o||l===a)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var o=t&&t.target&&t.target.src||a,r=new Error("Loading CSS chunk "+e+" failed.\n("+o+")");r.code="CSS_CHUNK_LOAD_FAILED",r.request=o,delete i[e],d.parentNode.removeChild(d),n(r)},d.href=a;var h=document.getElementsByTagName("head")[0];h.appendChild(d)}).then(function(){i[e]=0}));var o=a[e];if(0!==o)if(o)t.push(o[2]);else{var r=new Promise(function(t,n){o=a[e]=[t,n]});t.push(o[2]=r);var u,l=document.createElement("script");l.charset="utf-8",l.timeout=120,s.nc&&l.setAttribute("nonce",s.nc),l.src=c(e);var f=new Error;u=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=a[e];if(0!==n){if(n){var o=t&&("load"===t.type?"missing":t.type),i=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+o+": "+i+")",f.name="ChunkLoadError",f.type=o,f.request=i,n[1](f)}a[e]=void 0}};var d=setTimeout(function(){u({type:"timeout",target:l})},12e4);l.onerror=l.onload=u,document.head.appendChild(l)}return Promise.all(t)},s.m=e,s.c=o,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)s.d(n,o,function(t){return e[t]}.bind(null,o));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/",s.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var f=0;f<u.length;f++)t(u[f]);var d=l;r.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";var o=n("64a9"),i=n.n(o);i.a},"1ebd":function(e,t,n){},"2f73":function(e,t,n){},"4a08":function(e,t,n){},"4ffd":function(e,t,n){e.exports=n.p+"static/img/logo.ec723061.png"},"567f":function(e,t,n){"use strict";function o(e){if("number"!==typeof e)return e;e=new Date(e);var t=e.getFullYear(),n=e.getMonth()+1,o=e.getDate(),i=e.getHours(),a=e.getMinutes();return t+"-"+n+"-"+o+" "+i+":"+a}function i(e,t){var n=e.length<=t.length?e:t,o=e.length>t.length?e:t,i={},a=[];for(var r in n)i[n[r].id]=n[r];for(var c in o)i[o[c].id]&&a.push(i[o[c].id]);return a}t["a"]={parseTime:o,arrayIntersection:i}},"56d7":function(e,t,n){"use strict";n.r(t);n("cadf"),n("551c"),n("f751"),n("097d");var o=n("2b0e"),i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("navigator"),n("div",{staticClass:"main-content"},[n("keep-alive",{attrs:{include:["editor","error","viewnote","bookcommon"]}},[n("router-view")],1)],1)],1)},a=[],r=(n("7f7f"),n("a481"),function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"navigator"},[o("div",{staticClass:"logo-box",on:{click:function(t){return e.handleClick("/")}}},[o("img",{staticClass:"logo-img",attrs:{src:n("4ffd")}}),o("div",{directives:[{name:"show",rawName:"v-show",value:!(e.judgeMenu&&e.showPageTitle),expression:"!(judgeMenu && showPageTitle)"}]},[o("span",[e._v("Co")]),o("span",{staticClass:"note"},[e._v("Note")])]),o("div",{directives:[{name:"show",rawName:"v-show",value:e.judgeMenu,expression:"judgeMenu"}],staticClass:"page-title"},[e._v(e._s(e.showPageTitle))])]),e.judgeMenu&&e.ifLogin?o("div",{staticClass:"mobile-menu"},[o("div",{staticClass:"menu-icon",on:{click:e.clickMobileMenu}},[o("i",{staticClass:"el-icon-menu"})]),o("van-popup",{style:{height:"100%",width:"60%"},attrs:{position:"right"},model:{value:e.showPopup,callback:function(t){e.showPopup=t},expression:"showPopup"}},[o("div",{staticClass:"popup-cnt"},[o("div",{staticClass:"pop-logo"},[o("i",{staticClass:"el-icon-cloudy note"}),o("span",[e._v(" Co")]),o("span",{staticClass:"note"},[e._v("Note")])]),e._l(e.popupList,function(t){return o("div",{key:t.url,class:t.url===e.$route.path?"pop-active":"pop-opt",on:{click:function(n){return e.handleClick(t.url)}}},[o("i",{class:t.icon}),e._v("\n          "+e._s(t.name)+"\n        ")])})],2)])],1):o("div",{staticClass:"options-box"},e._l(e.navList,function(t){return o("div",{key:t.url,class:t.url===e.$route.path?"option-active":"option",on:{click:function(n){return e.handleClick(t.url)}}},[e._v(e._s(t.name))])}),0)])}),c=[],s=n("b21a"),u=s["a"].navObj,l={name:"Navigator",computed:{ifLogin:function(){return this.$store.state.ifLogin},navList:function(){if(this.$store.state.ifLogin){switch(this.$store.state.ssize){case 1:return[u.home,u.books,u.center];case 2:return[u.home,u.books,u.private,u.center]}return[]}return[u.home,u.login]},popupList:function(){return s["a"].mobilePaths},judgeMenu:function(){return 0===this.$store.state.ssize},showPageTitle:function(){return s["a"].pageTitleMap[this.$route.path]||""}},data:function(){return{showPopup:!1}},methods:{handleClick:function(e){var t=this;"logout"!==e?this.$route.path!==e&&(this.$router.push(e),this.showPopup=!1):this.$post("/api/logout").then(function(){t.$store.commit("logout"),"/"!==t.$route.path&&t.$router.push("/"),t.showPopup=!1})},clickMobileMenu:function(){this.showPopup=!0}}},f=l,d=(n("57fa"),n("2877")),h=Object(d["a"])(f,r,c,!1,null,"6228fcaf",null),p=h.exports,m={name:"app",components:{navigator:p},methods:{watchLoginPath:function(){-1!==this.$route.path.indexOf("/center")&&this.$router.replace("/login")}},beforeMount:function(){var e=this;window.onresize=function(){e.$store.commit("updateWidth",window.innerWidth)},this.$post("/api/check").then(function(t){e.$store.commit("login"),e.$store.commit("setAccount",t.account),e.$store.commit("setName",t.name)}).catch(function(){e.$store.commit("logout")}),this.$router.beforeEach(function(t,n,o){e.$store.state.ifLogin||-1===t.path.indexOf("/center")||o({replace:!0,path:"/404"}),o()})}},v=m,g=(n("034f"),Object(d["a"])(v,i,a,!1,null,null,null)),b=g.exports,k=n("8c4f"),w=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home-cnt"},[e.assertSmall?n("div",{staticClass:"note-head-small"},[n("el-input",{attrs:{size:"small",placeholder:"输入关键词",clearable:""},model:{value:e.searchFilter,callback:function(t){e.searchFilter=t},expression:"searchFilter"}}),n("el-button",{attrs:{size:"small"},on:{click:function(t){e.showPicker=!0}}},[e._v("Filter")]),n("van-popup",{attrs:{position:"bottom"},model:{value:e.showPicker,callback:function(t){e.showPicker=t},expression:"showPicker"}},[n("van-picker",{attrs:{"show-toolbar":"",columns:e.labelOptions},on:{cancel:function(t){e.showPicker=!1},confirm:e.pickerSelect}})],1)],1):e._e(),n("div",{staticClass:"home-note-box"},[e.assertSmall?e._e():n("div",{staticClass:"home-filter-box"},[n("el-input",{attrs:{size:"mini",placeholder:"输入关键词",clearable:""},model:{value:e.searchFilter,callback:function(t){e.searchFilter=t},expression:"searchFilter"}}),n("span",[e._v(" ")]),n("el-select",{attrs:{size:"mini",clearable:""},model:{value:e.selectFilter,callback:function(t){e.selectFilter=t},expression:"selectFilter"}},e._l(e.labelOptions,function(e){return n("el-option",{key:e,attrs:{label:e,value:e}})}),1)],1),e._l(e.notesFilter,function(t){return n("div",{key:t.id,staticClass:"home-note-each",on:{click:function(n){return e.viewNote(t)}}},[n("div",{staticClass:"home-note-title"},[n("el-tag",{attrs:{type:"danger",size:"mini"}},[e._v(e._s(t.label))]),n("div",{staticClass:"title"},[e._v(e._s(t.title))])],1),n("p",{staticClass:"home-note-content"},[e._v(e._s(t.content)+"...")]),n("div",{staticClass:"home-note-time"},[n("span",[e._v(e._s(t.modified))]),n("span",[e._v(" | ")]),n("span",[e._v(e._s(t.author))])])])})],2)])},y=[],_=n("75fc"),C=(n("ac6a"),n("5df3"),n("4f7f"),n("567f")),P={data:function(){return{notes:[],searchFilter:"",selectFilter:"",labelOptions:[],showPicker:!1}},computed:{notesFilter:function(){var e,t,n=this;return this.searchFilter||this.selectFilter?this.selectFilter&&(e=this.notes.filter(function(e){return e.label===n.selectFilter}),!this.searchFilter)?e:this.searchFilter&&(t=this.notes.filter(function(e){return-1!==e.title.indexOf(n.searchFilter)}),!this.selectFilter)?t:C["a"].arrayIntersection(e,t):this.notes},assertSmall:function(){return 0===this.$store.state.ssize}},methods:{viewNote:function(e){this.$router.push({path:"/view/"+e.id})},pickerSelect:function(e,t){this.selectFilter=e,this.showPicker=!1}},beforeMount:function(){var e=this;this.$post("/api/getnotes",{state:"save"}).then(function(t){var n=new Set;for(var o in t.notes)t.notes[o].modified=C["a"].parseTime(t.notes[o].modified),t.notes[o].label=t.notes[o].label.trim()||"未分类",t.notes[o].title=t.notes[o].title||"未设置标题",t.notes[o].author=t.notes[o].author||"未命名",n.add(t.notes[o].label);e.notes=t.notes,e.labelOptions=Object(_["a"])(n)})}},$=P,O=(n("6f2d"),Object(d["a"])($,w,y,!1,null,"1e0707ed",null)),x=O.exports;o["default"].use(k["a"]);var F=new k["a"]({routes:[{path:"/",name:"home",component:x},{path:"/login",name:"login",component:function(){return n.e("chunk-8504c7dc").then(n.bind(null,"a55b"))}},{path:"/view/:noteid",name:"view",component:function(){return Promise.all([n.e("chunk-6440f6d0"),n.e("chunk-3fc1a6d2")]).then(n.bind(null,"b1ac"))}},{path:"/center/note/:id",name:"note",component:function(){return n.e("chunk-06792728").then(n.bind(null,"fc0d"))}},{path:"/center/edit",name:"edit",component:function(){return Promise.all([n.e("chunk-6440f6d0"),n.e("chunk-701d3066")]).then(n.bind(null,"ffdd"))}},{path:"/center/setting",name:"setting",component:function(){return n.e("chunk-833d1566").then(n.bind(null,"5697"))}},{path:"/center",name:"center",component:function(){return n.e("chunk-caeb7a62").then(n.bind(null,"0ae3"))}},{path:"/404",name:"404",component:function(){return n.e("chunk-d9eafcd6").then(n.bind(null,"7af1"))}},{path:"*",redirect:{name:"404"}}]}),j=n("2f62");o["default"].use(j["a"]);var L=new j["a"].Store({state:{ifLogin:!1,account:"未登录",name:"未登录",screenWidth:window.innerWidth,screenSize:"large",ssize:0},getters:{ifLogin:function(e){return e.ifLogin}},mutations:{login:function(e){e.ifLogin||(e.ifLogin=!0)},logout:function(e){e.ifLogin&&(e.ifLogin=!1,e.account="未登录",e.name="未登录")},setAccount:function(e,t){e.account=t},setName:function(e,t){e.name=t||"未命名"},updateWidth:function(e,t){e.screenWidth=t,t<660?(e.screenSize="small",e.ssize=0):t<980?(e.screenSize="medium",e.ssize=1):(e.screenSize="large",e.ssize=2)}},actions:{}}),M=n("bc3a"),S=n.n(M),T={};function z(e){return{mode:"url",wait:e,previous:0,cache:null,caches:null,times:null,key:null}}function N(e,t){var n,o=this;return new Promise(function(i,a){var r=new Date;if(T[e])if("url"===T[e].mode){if(r-T[e].previous<T[e].wait)return void i(T[e].cache)}else if(n=T[e].key,r-T[e].times[t[n]]<T[e].wait)return void i(T[e].caches[t[n]]);S.a.post(e,t||{}).then(function(r){var c=r.data;if(0===c.status)return i(c.data),void(T[e]&&("url"===T[e].mode?(T[e].previous=new Date,T[e].cache=c.data):(n=T[e].key,T[e].times[t[n]]=new Date,T[e].caches[t[n]]=c.data)));100===c.status?(console.log("登录态无效"),-1!==o.$route.path.indexOf("/center")&&o.$router.replace("/login")):console.log("访问异常，状态码为",c.status),a(c.status)}).catch(function(e){console.log("接口异常",e)})})}function E(e,t,n){T[e]=z(t),n&&(T[e].mode="key",T[e].times={},T[e].caches={},T[e].key=n)}var A={post:N,setThrottle:E},D=(n("1ebd"),n("e4f7"),n("6ed5")),W=n.n(D),I=(n("a3cc"),n("f529")),q=n.n(I),B=(n("8a58"),n("e41f")),H=(n("5f5f"),n("f253")),J=(n("cda8"),n("df33")),G=n.n(J),K=(n("6a38"),n("18ff")),U=n.n(K),Y=(n("4a08"),n("defb")),Q=n.n(Y),R=(n("c55e"),n("b370")),V=n.n(R),X=(n("c7b2"),n("8bbc")),Z=n.n(X),ee=(n("bda2"),n("f3ad")),te=n.n(ee),ne=(n("2f73"),n("a578")),oe=n.n(ne),ie=(n("cb5e"),n("e772")),ae=n.n(ie),re=(n("d5ac"),n("4e4b")),ce=n.n(re),se=(n("d49f"),n("eedf")),ue=n.n(se);o["default"].use(ue.a),o["default"].use(ce.a),o["default"].use(ae.a),o["default"].use(oe.a),o["default"].use(te.a),o["default"].use(Z.a),o["default"].use(V.a),o["default"].use(Q.a),o["default"].use(U.a),o["default"].use(G.a),o["default"].use(H["a"]),o["default"].use(B["a"]),o["default"].prototype.$message=q.a,o["default"].prototype.$confirm=W.a.confirm,o["default"].config.productionTip=!1,o["default"].prototype.$post=A.post,A.setThrottle("/api/getnotes",5e3),A.setThrottle("/api/usernotes",5e3,"state"),new o["default"]({router:F,store:L,render:function(e){return e(b)}}).$mount("#app")},"57fa":function(e,t,n){"use strict";var o=n("79ff"),i=n.n(o);i.a},"64a9":function(e,t,n){},"6a38":function(e,t,n){},"6f2d":function(e,t,n){"use strict";var o=n("94cc"),i=n.n(o);i.a},"79ff":function(e,t,n){},"94cc":function(e,t,n){},a3cc:function(e,t,n){},b21a:function(e,t,n){"use strict";var o={bold:!0,italic:!0,header:!0,underline:!0,strikethrough:!0,mark:!0,superscript:!0,subscript:!0,quote:!0,ol:!0,ul:!0,link:!0,imagelink:!0,code:!0,table:!0,fullscreen:!0,readmodel:!1,htmlcode:!0,help:!1,undo:!0,redo:!0,trash:!0,save:!0,navigation:!0,alignleft:!0,aligncenter:!0,alignright:!0,subfield:!1,preview:!0},i={home:{url:"/",name:"HOME",icon:"el-icon-house"},login:{url:"/login",name:"LOGIN",icon:"el-icon-lock"},editor:{url:"/center/edit",name:"编辑笔记",icon:"el-icon-edit"},books:{url:"/center/note/books",name:"我的笔记",icon:"el-icon-notebook-1"},private:{url:"/center/note/private",name:"私人笔记",icon:"el-icon-lock"},center:{url:"/center",name:"个人中心",icon:"el-icon-user-solid"},setting:{url:"/center/setting",name:"个人信息",icon:"el-icon-setting"},drafts:{url:"/center/note/drafts",name:"草稿箱",icon:"el-icon-collection"},recycle:{url:"/center/note/recycle",name:"回收站",icon:"el-icon-delete"},logout:{url:"logout",name:"退出登录",icon:"el-icon-switch-button"}},a=[i.editor,i.books,i.private,i.setting,i.drafts,i.recycle,i.logout],r=[i.home,i.editor,i.books,i.private,i.setting,i.drafts,i.recycle,i.logout],c={"/center/edit":"编辑笔记","/center/note/books":"我的笔记","/center/note/private":"私人笔记","/center/note/drafts":"草稿箱","/center/note/recycle":"回收站","/center/setting":"个人信息"};t["a"]={toolbarsConfig:o,centerPaths:a,mobilePaths:r,pageTitleMap:c,navObj:i}},bda2:function(e,t,n){},c55e:function(e,t,n){},c7b2:function(e,t,n){},cb5e:function(e,t,n){},cda8:function(e,t,n){},d49f:function(e,t,n){},d5ac:function(e,t,n){},e4f7:function(e,t,n){}});
//# sourceMappingURL=app.e86c409f.js.map