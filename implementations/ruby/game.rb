require 'json'
s = JSON.parse(File.read('current_state.json'))
cell = (ENV['CELL'] || "").upcase
action = ENV['ACTION'] || "put"

if action == 'reset'
  s = {"board"=>[["","",""],["","",""],["","",""]], "turn"=>"X", "winner"=>nil, "log"=>[]}
elsif !cell.empty? && !s['winner']
  r, c = cell[0].ord - 65, cell[1].to_i - 1
  if r>=0 && r<3 && c>=0 && c<3 && s['board'][r][c] == ""
    s['board'][r][c] = s['turn']
    lns = [[0,0,0,1,0,2],[1,0,1,1,1,2],[2,0,2,1,2,2],[0,0,1,0,2,0],[0,1,1,1,2,1],[0,2,1,2,2,2],[0,0,1,1,2,2],[0,2,1,1,2,0]]
    win = lns.any? { |l| !s['board'][l[0]][l[1]].empty? && s['board'][l[0]][l[1]] == s['board'][l[2]][l[3]] && s['board'][l[2]][l[3]] == s['board'][l[4]][l[5]] }
    if win then s['winner'] = s['turn']
    elsif s['board'].flatten.none?(&:empty?) then s['winner'] = 'draw'
    else s['turn'] = (s['turn'] == "X" ? "O" : "X")
    end
  end
end
File.write('current_state.json', JSON.pretty_generate(s))
