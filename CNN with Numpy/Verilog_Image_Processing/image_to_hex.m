b = imread('download.jpg')
k =1;
for i = 512:-1:1
for j = 1:768
    a(k) = b(i, j,1);
    a(k+1) = b(i,j,2);
    a(k+2) = b(i,j,3);
    k = k+ 3;
end
end 
 fid = fopen('download.hex', 'wt');
 fprintf(fid, '%x\n', a);
 disp('text file write done'); disp(' ');
 fclose(fid);