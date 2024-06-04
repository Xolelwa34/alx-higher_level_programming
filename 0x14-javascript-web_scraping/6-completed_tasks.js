#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let c = 0; c < body.length; ++c) {
      const userId = body[c].userId;
      const completed = body[c].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
