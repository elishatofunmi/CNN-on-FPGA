% function handling


y = 7;
fh = @(x)x.^2 + 10 * (y);
k = fh(3);

s = functions(fh);

s.workspace{1};


