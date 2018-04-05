function [mean] = get_mean(vector)
iter = size(vector);
iter = iter(2);
hold = 0;
for n = 1:iter
    
    hold = hold + vector(1,n);
end
total = size(vector);
mean = hold/(total(2));
