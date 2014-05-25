function N= count_nodes( root )
	
N=1;
if ~isempty(root.left)
		N=N+count_nodes(root.left);
end
if ~isempty(root.right)
    N=N+count_nodes(root.right);
end

end

