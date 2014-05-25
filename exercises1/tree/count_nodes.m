function N= count_nodes( root )
	
N=1;
if ~isempty(root.children)
    for ii=1:length(root.children)
		N=N+count_nodes(root.children(ii));
    end
end

end

