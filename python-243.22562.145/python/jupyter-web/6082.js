"use strict";(self.webpackChunkjupyter_web=self.webpackChunkjupyter_web||[]).push([[6082],{76082:(x,t,c)=>{function u(d){var n,l;d?(n=/^(exx?|(ld|cp)([di]r?)?|[lp]ea|pop|push|ad[cd]|cpl|daa|dec|inc|neg|sbc|sub|and|bit|[cs]cf|x?or|res|set|r[lr]c?a?|r[lr]d|s[lr]a|srl|djnz|nop|[de]i|halt|im|in([di]mr?|ir?|irx|2r?)|ot(dmr?|[id]rx|imr?)|out(0?|[di]r?|[di]2r?)|tst(io)?|slp)(\.([sl]?i)?[sl])?\b/i,l=/^(((call|j[pr]|rst|ret[in]?)(\.([sl]?i)?[sl])?)|(rs|st)mix)\b/i):(n=/^(exx?|(ld|cp|in)([di]r?)?|pop|push|ad[cd]|cpl|daa|dec|inc|neg|sbc|sub|and|bit|[cs]cf|x?or|res|set|r[lr]c?a?|r[lr]d|s[lr]a|srl|djnz|nop|rst|[de]i|halt|im|ot[di]r|out[di]?)\b/i,l=/^(call|j[pr]|ret[in]?|b_?(call|jump))\b/i);var b=/^(af?|bc?|c|de?|e|hl?|l|i[xy]?|r|sp)\b/i,a=/^(n?[zc]|p[oe]?|m)\b/i,p=/^([hl][xy]|i[xy][hl]|slia|sll)\b/i,o=/^([\da-f]+h|[0-7]+o|[01]+b|\d+d?)\b/i;return{name:"z80",startState:function(){return{context:0}},token:function(e,i){if(e.column()||(i.context=0),e.eatSpace())return null;var r;if(e.eatWhile(/\w/)){if(d&&e.eat(".")&&e.eatWhile(/\w/),r=e.current(),!e.indentation())return e.match(o)?"number":null;if((1==i.context||4==i.context)&&b.test(r))return i.context=4,"variable";if(2==i.context&&a.test(r))return i.context=4,"variableName.special";if(n.test(r))return i.context=1,"keyword";if(l.test(r))return i.context=2,"keyword";if(4==i.context&&o.test(r))return"number";if(p.test(r))return"error"}else{if(e.eat(";"))return e.skipToEnd(),"comment";if(e.eat('"')){for(;(r=e.next())&&'"'!=r;)"\\"==r&&e.next();return"string"}if(e.eat("'")){if(e.match(/\\?.'/))return"number"}else if(e.eat(".")||e.sol()&&e.eat("#")){if(i.context=5,e.eatWhile(/\w/))return"def"}else if(e.eat("$")){if(e.eatWhile(/[\da-f]/i))return"number"}else if(e.eat("%")){if(e.eatWhile(/[01]/))return"number"}else e.next()}return null}}}c.r(t),c.d(t,{ez80:()=>s,z80:()=>f});const f=u(!1),s=u(!0)}}]);