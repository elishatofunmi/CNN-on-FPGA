function[hNest, hLocal] = functionsExample(v)


hNest = @nestFunction;
hlocal = @localFunction;

    function y = nestFunction(x)
        y = x + v;
    end
end

function y = localFunction(z)
y = z + 1;

% s1 = functions(hNest);

% s2 = functions(hLocal);
end



