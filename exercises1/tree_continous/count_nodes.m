function N= count_nodes( root )

if isempty(root.left) && isempty(root.right)    %leaf node
    N=0;
else   
    N=1;
end

if ~isempty(root.left)
		N=N+count_nodes(root.left);
end
if ~isempty(root.right)
    N=N+count_nodes(root.right);
end

end

