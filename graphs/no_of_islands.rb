def dfs(grid, m, n, i, j, visited)
  # puts "dfs called with #{i}, #{j} | grid[i]: #{grid[i]}"
  return if grid[i][j] == '0' || visited[i][j]
  visited[i][j] = true
  dfs(grid, m, n, i - 1, j, visited) if i > 0
  dfs(grid, m, n, i + 1, j, visited) if i < m - 1
  dfs(grid, m, n, i, j - 1, visited) if j > 0
  dfs(grid, m, n, i, j + 1, visited) if j < n - 1
end

def cc(grid, m, n)
  count = 0
  visited = Array.new(m) { Array.new(n, false) }
  0.upto(m - 1) do |i|
    0.upto(n - 1) do |j|
      next if grid[i][j] == '0' || visited[i][j]
      dfs(grid, m, n, i, j, visited)
      count += 1
    end
  end
  count
end

# @param {Character[][]} grid
# @return {Integer}
def num_islands(grid)
  return 0 if grid.nil? || grid.empty?
  m, n = grid.size, grid[0].size
  # puts "m: #{m} | n: #{n}"
  cc(grid, m, n)
end

grid = ["11110", "11010", "11000", "00000"]
puts num_islands(grid)

grid2 = ['100','000', '001']
puts num_islands(grid2)

grid3 = ["111111", "100001", "101101", "100001", "111111"]
puts num_islands(grid3)