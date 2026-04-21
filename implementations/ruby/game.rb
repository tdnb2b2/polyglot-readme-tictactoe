require 'json'

state = JSON.parse(File.read('current_state.json'))

cell = (ENV['CELL'] || '').upcase
action = ENV['ACTION'] || 'put'

def check_winner(b)
  lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  flat = b.flatten
  lines.each do |l|
    return flat[l[0]] if flat[l[0]] != '' && flat[l[0]] == flat[l[1]] && flat[l[0]] == flat[l[2]]
  end
  nil
end

if action == 'reset'
  is_full = state['board'].flatten.all? { |c| c != '' }
  if state['winner'] || is_full
    state = {"board" => [["","",""],["","",""],["","",""]], "turn" => "X", "winner" => nil, "log" => []}
  end
elsif cell != '' && !state['winner']
  r = cell[1].to_i - 1
  c = cell[0].ord - 'A'.ord
  if r >= 0 && r < 3 && c >= 0 && c < 3 && state['board'][r][c] == ''
    state['board'][r][c] = state['turn']
    state['log'] << {"player" => state['turn'], "cell" => cell}
    win = check_winner(state['board'])
    if win
      state['winner'] = win
    elsif state['board'].flatten.all? { |x| x != '' }
      state['winner'] = 'draw'
    else
      state['turn'] = state['turn'] == 'X' ? 'O' : 'X'
    end
  end
end

File.write('current_state.json', JSON.pretty_generate(state))
