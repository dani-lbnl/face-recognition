function out = l5(G,N,K)
[col,row]=size(G);
% Valores dos blocos
aa = 1:N:row;
bb = 1:K:col;
[ii,jj] = ndgrid(aa,bb);
out = arrayfun(@(x,y) G(x:x+N-1,y:y+K-1),jj,ii,'un',0);