(function(e){function t(t){for(var r,a,c=t[0],s=t[1],u=t[2],l=0,f=[];l<c.length;l++)a=c[l],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&f.push(o[a][0]),o[a]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(e[r]=s[r]);d&&d(t);while(f.length)f.shift()();return i.push.apply(i,u||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,a=1;a<n.length;a++){var c=n[a];0!==o[c]&&(r=!1)}r&&(i.splice(t--,1),e=s(s.s=n[0]))}return e}var r={},a={app:0},o={app:0},i=[];function c(e){return s.p+"static/js/"+({}[e]||e)+"."+{"chunk-2d2378a7":"5712b482","chunk-56e3ef01":"d69f7f48","chunk-5bb07c56":"2475288d","chunk-6440f6d0":"3dadad78","chunk-7efbfb6b":"e1b80e5a","chunk-7f66ab31":"01dd33f4","chunk-6da730de":"4d7d52cc","chunk-98f54998":"621b73a2","chunk-d23cddbe":"a73f5f60"}[e]+".js"}function s(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(e){var t=[],n={"chunk-56e3ef01":1,"chunk-5bb07c56":1,"chunk-6440f6d0":1,"chunk-7efbfb6b":1,"chunk-7f66ab31":1,"chunk-6da730de":1,"chunk-98f54998":1,"chunk-d23cddbe":1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise(function(t,n){for(var r="static/css/"+({}[e]||e)+"."+{"chunk-2d2378a7":"31d6cfe0","chunk-56e3ef01":"2ee6eb49","chunk-5bb07c56":"a2af3a6f","chunk-6440f6d0":"b35fc6d0","chunk-7efbfb6b":"99bd7f1f","chunk-7f66ab31":"56c5a55e","chunk-6da730de":"949c397c","chunk-98f54998":"342fcea1","chunk-d23cddbe":"2a0e2d2d"}[e]+".css",o=s.p+r,i=document.getElementsByTagName("link"),c=0;c<i.length;c++){var u=i[c],l=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(l===r||l===o))return t()}var f=document.getElementsByTagName("style");for(c=0;c<f.length;c++){u=f[c],l=u.getAttribute("data-href");if(l===r||l===o)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var r=t&&t.target&&t.target.src||o,i=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");i.code="CSS_CHUNK_LOAD_FAILED",i.request=r,delete a[e],d.parentNode.removeChild(d),n(i)},d.href=o;var h=document.getElementsByTagName("head")[0];h.appendChild(d)}).then(function(){a[e]=0}));var r=o[e];if(0!==r)if(r)t.push(r[2]);else{var i=new Promise(function(t,n){r=o[e]=[t,n]});t.push(r[2]=i);var u,l=document.createElement("script");l.charset="utf-8",l.timeout=120,s.nc&&l.setAttribute("nonce",s.nc),l.src=c(e);var f=new Error;u=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;f.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",f.name="ChunkLoadError",f.type=r,f.request=a,n[1](f)}o[e]=void 0}};var d=setTimeout(function(){u({type:"timeout",target:l})},12e4);l.onerror=l.onload=u,document.head.appendChild(l)}return Promise.all(t)},s.m=e,s.c=r,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)s.d(n,r,function(t){return e[t]}.bind(null,r));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/",s.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var f=0;f<u.length;f++)t(u[f]);var d=l;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";var r=n("64a9"),a=n.n(r);a.a},"3f85":function(e,t,n){},4933:function(e,t,n){"use strict";var r=n("3f85"),a=n.n(r);a.a},"4ffd":function(e,t,n){e.exports=n.p+"static/img/logo.ec723061.png"},"567f":function(e,t,n){"use strict";function r(e){e=new Date(parseInt(1e3*e));var t=e.getFullYear(),n=e.getMonth()+1,r=e.getDate(),a=e.getHours(),o=e.getMinutes();return t+"-"+n+"-"+r+" "+a+":"+o}function a(e,t){var n=e.length<=t.length?e:t,r=e.length>t.length?e:t,a={},o=[];for(var i in n)a[n[i].id]=n[i];for(var c in r)a[r[c].id]&&o.push(a[r[c].id]);return o}t["a"]={parseTime:r,arrayIntersection:a}},"56d7":function(e,t,n){"use strict";n.r(t);n("cadf"),n("551c"),n("f751"),n("097d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("navigator"),n("div",{staticClass:"main-content"},[n("keep-alive",{attrs:{include:["editor","error","viewnote"]}},[n("router-view")],1)],1)],1)},o=[],i=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"navigator"},[r("div",{staticClass:"logo-box",on:{click:function(t){return e.handleClick("/")}}},[r("img",{staticClass:"logo-img",attrs:{src:n("4ffd")}}),r("span",[e._v("CoNote")])]),e.ifLogin?r("div",{staticClass:"avatar-box",on:{click:function(t){return e.handleClick("/center")}}},[r("i",{staticClass:"el-icon-s-custom"})]):r("div",{staticClass:"options-box"},[r("div",{staticClass:"option",on:{click:function(t){return e.handleClick("/login")}}},[e._v("登录")])])])},c=[],s=n("b21a"),u={name:"Navigator",computed:{ifLogin:function(){return this.$store.state.ifLogin},navList:function(){return this.$store.state.ifLogin?s["a"].navListLogin:s["a"].navListNotLogin}},data:function(){return{}},methods:{handleClick:function(e){this.$route.path!==e&&this.$router.push(e)}}},l=u,f=(n("4933"),n("2877")),d=Object(f["a"])(l,i,c,!1,null,"ab9cf578",null),h=d.exports,p={name:"app",components:{navigator:h},beforeMount:function(){var e=this;this.$router.beforeEach(function(t,n,r){e.$store.state.ifLogin||-1!==t.path.indexOf("/center")&&r({replace:!0,path:"/404"}),r()})}},b=p,m=(n("034f"),Object(f["a"])(b,a,o,!1,null,null,null)),v=m.exports,g=n("8c4f"),k=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"home"},[n("book",{attrs:{home:!0}})],1)},y=[],w=n("d33e"),_={name:"home",components:{book:w["a"]},methods:{}},C=_,x=Object(f["a"])(C,k,y,!1,null,"2382871b",null),O=x.exports;r["default"].use(g["a"]);var L=new g["a"]({routes:[{path:"/",name:"home",component:O},{path:"/login",name:"register",component:function(){return n.e("chunk-98f54998").then(n.bind(null,"73cf"))}},{path:"/view/:noteid",name:"view",component:function(){return Promise.all([n.e("chunk-6440f6d0"),n.e("chunk-7efbfb6b")]).then(n.bind(null,"b1ac"))}},{path:"/center/books",name:"books",component:function(){return n.e("chunk-2d2378a7").then(n.bind(null,"fc0d"))}},{path:"/center/recycle",name:"recycle",component:function(){return n.e("chunk-6da730de").then(n.bind(null,"4cf3"))}},{path:"/center/edit",name:"edit",component:function(){return Promise.all([n.e("chunk-6440f6d0"),n.e("chunk-7f66ab31")]).then(n.bind(null,"ffdd"))}},{path:"/center/drafts",name:"drafts",component:function(){return n.e("chunk-56e3ef01").then(n.bind(null,"b9f3"))}},{path:"/center",name:"center",component:function(){return n.e("chunk-5bb07c56").then(n.bind(null,"0ae3"))}},{path:"/404",name:"404",component:function(){return n.e("chunk-d23cddbe").then(n.bind(null,"7af1"))}},{path:"*",redirect:{name:"404"}}]}),F=n("2f62");r["default"].use(F["a"]);var $=new F["a"].Store({state:{ifLogin:!0},getters:{ifLogin:function(e){return e.ifLogin}},mutations:{change:function(e,t){e.ifLogin=t}},actions:{}}),j=(n("9e1f"),n("450d"),n("6ed5")),E=n.n(j),P=(n("0fb7"),n("f529")),N=n.n(P),S=(n("a7cc"),n("df33")),T=n.n(S),M=(n("bd49"),n("18ff")),A=n.n(M),D=(n("960d"),n("defb")),I=n.n(D),q=(n("cb70"),n("b370")),B=n.n(q),z=(n("cbb5"),n("8bbc")),H=n.n(z),J=(n("10cb"),n("f3ad")),K=n.n(J),U=(n("aaa5"),n("a578")),Y=n.n(U),G=(n("6611"),n("e772")),Q=n.n(G),R=(n("1f1a"),n("4e4b")),V=n.n(R),W=(n("1951"),n("eedf")),X=n.n(W);r["default"].use(X.a),r["default"].use(V.a),r["default"].use(Q.a),r["default"].use(Y.a),r["default"].use(K.a),r["default"].use(H.a),r["default"].use(B.a),r["default"].use(I.a),r["default"].use(A.a),r["default"].use(T.a),r["default"].prototype.$message=N.a,r["default"].prototype.$confirm=E.a.confirm;var Z=n("bc3a"),ee=n.n(Z);function te(e,t){return new Promise(function(n,r){ee.a.post(e,t||{}).then(function(e){var t=e.data;0!==t.status||void 0===t.data?(console.log("访问异常，状态码为"+t.status),r(t.status)):n(t.data)}).catch(function(e){console.log("接口异常",e)})})}r["default"].prototype.$post=te,r["default"].config.productionTip=!1,new r["default"]({router:L,store:$,render:function(e){return e(v)}}).$mount("#app")},"64a9":function(e,t,n){},b21a:function(e,t,n){"use strict";var r={bold:!0,italic:!0,header:!0,underline:!0,strikethrough:!0,mark:!0,superscript:!0,subscript:!0,quote:!0,ol:!0,ul:!0,link:!0,imagelink:!0,code:!0,table:!0,fullscreen:!0,readmodel:!1,htmlcode:!0,help:!1,undo:!0,redo:!0,trash:!0,save:!0,navigation:!0,alignleft:!0,aligncenter:!0,alignright:!0,subfield:!1,preview:!0},a=[{url:"/edit",name:"添加笔记"},{url:"/books",name:"我的笔记"},{url:"/drafts",name:"草稿箱"},{url:"/recycle",name:"回收站"},{url:"/center",name:"个人中心"}],o=[{url:"/register",name:"注册"},{url:"/login",name:"登录"}],i=[{url:"/center/edit",name:"添加笔记",icon:"el-icon-edit"},{url:"/center/books",name:"我的笔记",icon:"el-icon-notebook-1"},{url:"/center/drafts",name:"草稿箱",icon:"el-icon-collection"},{url:"/center/recycle",name:"回收站",icon:"el-icon-delete"}];t["a"]={toolbarsConfig:r,navListLogin:a,navListNotLogin:o,centerPaths:i}},b5a0:function(e,t,n){},d33e:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"note-cnt"},[n("div",{staticClass:"filter-box"},[n("el-input",{staticStyle:{width:"200px"},attrs:{placeholder:"输入关键词",clearable:""},model:{value:e.searchFilter,callback:function(t){e.searchFilter=t},expression:"searchFilter"}}),n("span",[e._v("  ")]),n("el-select",{staticStyle:{width:"200px"},attrs:{clearable:""},model:{value:e.selectFilter,callback:function(t){e.selectFilter=t},expression:"selectFilter"}},e._l(e.labelOptions,function(e){return n("el-option",{key:e,attrs:{label:e,value:e}})}),1)],1),n("div",{staticClass:"note-box"},e._l(e.notesFilter,function(t){return n("div",{key:t.id,staticClass:"note-each-box"},[n("div",{staticClass:"note-layout"},[n("div",{staticClass:"note-tag-title",on:{click:function(n){return e.viewNote(t)}}},[n("el-tag",{attrs:{type:"danger",size:"mini"}},[e._v(e._s(t.label||"未分类"))]),n("div",{staticClass:"note-title"},[e._v(e._s(t.title||"未设置标题"))])],1),e.home?e._e():n("div",[n("el-dropdown",{attrs:{trigger:"click"},on:{command:function(n){return e.handleOption(n,t.id)}}},[n("el-button",{attrs:{icon:"el-icon-setting",plain:"",size:"mini",circle:""}}),n("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[n("el-dropdown-item",{attrs:{command:"revise"}},[e._v("修改")]),n("el-dropdown-item",{attrs:{command:"remove"}},[e._v("删除")])],1)],1)],1)]),n("div",{staticClass:"note-content",on:{click:function(n){return e.viewNote(t)}}},[e._v(e._s(t.content)+"...")]),n("div",{staticClass:"note-layout",on:{click:function(n){return e.viewNote(t)}}},[n("div",{staticClass:"note-time"},[e._v(e._s(t.modified))])])])}),0)])},a=[],o=n("75fc"),i=(n("ac6a"),n("5df3"),n("4f7f"),n("567f")),c={props:["home"],data:function(){return{notes:[],searchFilter:"",selectFilter:"",labelOptions:[]}},computed:{notesFilter:function(){var e,t,n=this;return this.searchFilter||this.selectFilter?this.selectFilter&&(e=this.notes.filter(function(e){return e.label===n.selectFilter}),!this.searchFilter)?e:this.searchFilter&&(t=this.notes.filter(function(e){return-1!==e.title.indexOf(n.searchFilter)}),!this.selectFilter)?t:i["a"].arrayIntersection(e,t):this.notes}},methods:{handleOption:function(e,t){var n=this;"revise"===e?this.$router.push({name:"edit",params:{noteid:t}}):"remove"===e&&this.$post("/api/notestate",{noteid:t,state:"del"}).then(function(){var e=0;for(e=0;e<n.notes.length;++e)if(n.notes[e].id===t)break;n.notes.splice(e,1),n.$message.success("删除成功")})},viewNote:function(e){this.$router.push({path:"/view/"+e.id})}},beforeMount:function(){var e=this;this.$post("/api/getnotes",{state:"save"}).then(function(t){var n=new Set;for(var r in t.notes)t.notes[r].modified=i["a"].parseTime(t.notes[r].modified),t.notes[r].label=t.notes[r].label.trim()||"未分类",n.add(t.notes[r].label);e.notes=t.notes,e.labelOptions=Object(o["a"])(n)})}},s=c,u=(n("f8e4"),n("2877")),l=Object(u["a"])(s,r,a,!1,null,"067ee908",null);t["a"]=l.exports},f8e4:function(e,t,n){"use strict";var r=n("b5a0"),a=n.n(r);a.a}});
//# sourceMappingURL=app.2754be2e.js.map