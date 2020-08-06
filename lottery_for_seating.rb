#! /usr/bin/env ruby

# input: member_list_file
# format
# number[tab]name

SEATS = ["A", "A", "A", "A", "B", "B", "B", "B"]

## Load member list from file
member_list_file = ARGV[0]
members = []
File.open(member_list_file).each do |l|
    next if /^\#/.match(l)
    ary = l.chomp.split(/\t/)
    name = ary[1]
    members << name
end
puts "# members are being loaded ..."
puts "# #{members.length} members found"

## Prepare seats and randomize them
seats = SEATS
seats_shuffled = seats.shuffle

raise unless members.length == seats.length

sleep 2
puts "# We have #{seats.length} seats with #{seats.sort.uniq.length} categories"
puts "# Seats are randomized..."
sleep 2
puts "# done"
puts "# Let's see your new seats ..."
sleep 2

## Pairing members and seats
pair = Hash.new
members.each_with_index do |m, i|
    pair[m] = seats_shuffled[i]
    puts  "#{m} => #{pair[m]}"
    sleep 2
end

## Display summary
puts ""
puts "# Summary"
pair.values.sort.uniq.each do |v|
    print "Category #{v}: "
    print pair.select{|m, s| s == v}.keys.join(", ") + "\n"
end
