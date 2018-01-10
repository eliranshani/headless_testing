var stats = require('docker-stats');
var through = require('through2');
var config = {
    seconds : true,
    keep: true,
    interval: 500,
    // pattern: "[^-]*-(.*)",
    metrics: {
        one: {
            aggregator: "growth",
            color: "yellow,bold"
        },
    }
};
var turtle = (require('turtle-race'))(config);

stats({statsinterval: 1}).pipe(through.obj(function(container, enc, cb) {
    turtle.metric(container.name, "cpu")
        .push(container.stats.cpu_stats.cpu_usage.cpu_percent);
    turtle.metric(container.name, "memory")
        .push(container.stats.memory);
    return cb();
}));