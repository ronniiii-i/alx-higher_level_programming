#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
    // callMeMoby(x - 1, theFunction);
  }
}
module.exports = {callMeMoby};
