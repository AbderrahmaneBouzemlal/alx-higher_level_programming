#!/usr/bin/node
exports.esrever = function (list) {
  let reversed = Array(list.length);
  for (let i = 0; i < list.length; i++) {
    reversed[i] = list[list.length - 1 - i];
  }
  return reversed;
}
