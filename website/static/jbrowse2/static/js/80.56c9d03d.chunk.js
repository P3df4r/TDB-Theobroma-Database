(this["webpackJsonp@jbrowse/web"]=this["webpackJsonp@jbrowse/web"]||[]).push([[80],{2531:function(e,t,r){"use strict";r.r(t),r.d(t,"default",(function(){return d}));var n=r(87),a=r.n(n),i=r(83),c=r(91),u=r(90),s=r(94),o=r(96),f=r(97),b=r(160),p=r(134),h=r(187),v=r(182),l=r(2398),m=r(82),d=function(e){Object(o.a)(r,e);var t=Object(f.a)(r);function r(e,n,a){var i;return Object(u.a)(this,r),(i=t.call(this,e,n,a)).twobit=void 0,i.chromSizesData=void 0,i.chromSizesData=i.initChromSizes(),i.twobit=new l.TwoBitFile({filehandle:Object(p.openLocation)(Object(m.readConfObject)(e,"twoBitLocation"),i.pluginManager)}),i}return Object(s.a)(r,[{key:"initChromSizes",value:function(){var e=Object(c.a)(a.a.mark((function e(){var t,r,n;return a.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if("/path/to/default.chrom.sizes"===(t=Object(m.readConfObject)(this.config,"chromSizesLocation")).uri||""===t.uri){e.next=7;break}return r=Object(p.openLocation)(t,this.pluginManager),e.next=5,r.readFile("utf8");case 5:return n=e.sent,e.abrupt("return",Object.fromEntries(null===n||void 0===n?void 0:n.split("\n").filter((function(e){return!!e.trim()})).map((function(e){var t=e.split("\t"),r=Object(i.a)(t,2);return[r[0],+r[1]]}))));case 7:return e.abrupt("return",void 0);case 8:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"getRefNames",value:function(){var e=Object(c.a)(a.a.mark((function e(){var t;return a.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.chromSizesData;case 2:if(!(t=e.sent)){e.next=5;break}return e.abrupt("return",Object.keys(t));case 5:return e.abrupt("return",this.twobit.getSequenceNames());case 6:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"getRegions",value:function(){var e=Object(c.a)(a.a.mark((function e(){var t,r;return a.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.chromSizesData;case 2:if(!(t=e.sent)){e.next=5;break}return e.abrupt("return",Object.keys(t).map((function(e){return{refName:e,start:0,end:t[e]}})));case 5:return e.next=7,this.twobit.getSequenceSizes();case 7:return r=e.sent,e.abrupt("return",Object.keys(r).map((function(e){return{refName:e,start:0,end:r[e]}})));case 9:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"getFeatures",value:function(e){var t=this,r=e.refName,n=e.start,i=e.end;return Object(h.ObservableCreate)(function(){var e=Object(c.a)(a.a.mark((function e(c){var u,s,o;return a.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,t.twobit.getSequenceSize(r);case 2:return u=e.sent,s=void 0!==u?Math.min(u,i):i,e.next=6,t.twobit.getSequence(r,n,s);case 6:(o=e.sent)&&c.next(new v.a({id:"".concat(r," ").concat(n,"-").concat(s),data:{refName:r,start:n,end:s,seq:o}})),c.complete();case 9:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}())}},{key:"freeResources",value:function(){}}]),r}(b.BaseFeatureDataAdapter)}}]);
//# sourceMappingURL=80.56c9d03d.chunk.js.map