#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let i = 0; i < 3; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
