% loops 

N = 100;
f(1) = 1; % create an array f and set first value to 1
f(2) = 1; % create an array f and set second value to 1

for n = 3:N
    f(n) = f(n-1) +f(n-2);
end
f(1:10);


% conditional statements

num = randi(100);
if num < 34
    sz = 'low'
elseif num < 67
    sz = 'medium'
else
    sz = 'high'
end