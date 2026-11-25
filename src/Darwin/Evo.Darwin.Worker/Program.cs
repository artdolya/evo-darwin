var builder = Host.CreateApplicationBuilder(args);

// No message consumer is registered yet. The process starts and waits until it is stopped.
var host = builder.Build();

host.Run();
