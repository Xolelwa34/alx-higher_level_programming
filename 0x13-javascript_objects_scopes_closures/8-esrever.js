#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (array, create) {
    array.push(create);
    return array;
  }, []);
};
