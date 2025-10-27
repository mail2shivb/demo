Excellent ✅

We’ll now generate **Section 1 – Java (7 → 21)**
**100 Advanced Interview Questions + Full Answers**
*(optimized for Senior Java Developer / Lead Engineer interviews at banks, fintechs, or cloud-native projects)*

---

# 🧠 **Section 1 – Advanced Java Interview Questions (100 Q&A)**

---

### **1. What are the key differences between Java 7, 8, 11, 17, and 21 LTS releases?**

Java 8 introduced functional programming (Streams, Lambdas), Java 11 added the HTTP Client API and local-variable syntax for lambdas, Java 17 delivered pattern matching and sealed classes, while Java 21 introduced virtual threads (Project Loom), record patterns, and sequenced collections.
Each LTS emphasizes performance, garbage-collection improvements (G1→ZGC→Shenandoah), and modular JVM architecture.

---

### **2. Explain how Virtual Threads differ from Platform Threads.**

Virtual Threads (Project Loom) are lightweight, scheduled by the JVM rather than OS, enabling millions of concurrent tasks without heavy thread-pool management.
They remove the scalability bottleneck of blocking I/O by allowing synchronous code with near-async throughput.

---

### **3. Describe the internal structure of the JVM memory model.**

The JVM Memory Model (JMM) defines **Heap**, **Stack**, **Metaspace**, **Code Cache**, and **Native Memory**.
Heap holds objects, stack holds method frames, metaspace holds class metadata (since Java 8), code cache stores JIT compiled code. The JMM ensures visibility and ordering of reads/writes via `volatile`, `synchronized`, and `final`.

---

### **4. What happens when you run `java HelloWorld`?**

1. **Bootstrap ClassLoader** loads `java.lang.Object`.
2. **AppClassLoader** loads HelloWorld.
3. JVM creates a main thread and invokes `public static void main`.
4. JIT compiles hot methods, allocates objects on the heap, triggers GC when needed.
5. On exit, shutdown hooks run and daemon threads are stopped.

---

### **5. How does the JIT compiler optimize code?**

The JIT (Just-In-Time) compiler dynamically compiles bytecode to native machine code, applying optimizations like method inlining, loop unrolling, escape analysis (stack allocation), and speculative execution based on runtime profiling.

---

### **6. What is Escape Analysis and why is it useful?**

Escape Analysis detects if an object escapes the scope of a method.
If it does not, the JIT allocates it on the stack instead of the heap, reducing GC pressure and boosting performance.

---

### **7. What are Record classes introduced in Java 14/16?**

Records are immutable data carriers that auto-generate `equals`, `hashCode`, `toString`, and constructors.

```java
public record User(String name, int age) {}
```

They are ideal for DTOs and work beautifully with pattern matching.

---

### **8. How do Record Patterns enhance pattern matching (Java 21)?**

Record patterns allow deconstruction of records directly in `switch` or `instanceof` checks:

```java
if (obj instanceof Point(int x, int y)) { … }
```

This reduces boilerplate and supports nested data decomposition.

---

### **9. Explain Pattern Matching for `instanceof`.**

Introduced in Java 16:

```java
if (obj instanceof String s) { … }
```

Eliminates redundant casts and enhances type-safety.

---

### **10. How do Sealed Classes improve type hierarchies?**

Sealed classes restrict which classes can extend or implement them using the `permits` clause, enforcing stronger domain control and pattern-matching exhaustiveness.

---

### **11. Difference between `var`, `record`, and `sealed` keywords.**

* `var` → local type inference only
* `record` → immutable data carrier
* `sealed` → restricted inheritance hierarchy

---

### **12. What are Sequenced Collections (Java 21)?**

They introduce a consistent API across `List`, `Set`, and `Map` for iteration order: `getFirst()`, `getLast()`, `reversed()`, simplifying bidirectional traversal.

---

### **13. Explain Functional Interfaces and their use in Java 8+.**

A Functional Interface contains exactly one abstract method (e.g. `Runnable`, `Predicate`).
They enable Lambda expressions and method references — cornerstone of functional programming in Java.

---

### **14. How do Streams differ from Collections?**

Collections store data; Streams describe pipelines of operations on data.
Streams are lazy, can be parallel, and promote declarative functional style.

---

### **15. What are Intermediate vs Terminal Stream operations?**

Intermediate: `map`, `filter`, `sorted` (lazy).
Terminal: `collect`, `count`, `forEach`.
Pipeline executes only upon a terminal operation.

---

### **16. What are Collector and Reduce operations?**

`reduce()` combines elements using an accumulator;
`Collectors` provide ready-made reductions (e.g. `groupingBy`, `summingInt`).

---

### **17. How does Parallel Stream work internally?**

Uses Fork/Join framework to split tasks across multiple threads. Be careful with shared mutable state and unordered collections.

---

### **18. What is a CompletableFuture and how is it different from Future?**

`CompletableFuture` supports chained async callbacks (`thenApply`, `thenCompose`), error handling, and combinators, while `Future` is blocking and cannot be completed manually.

---

### **19. How do you handle exceptions in CompletableFuture?**

Use `exceptionally()`, `handle()`, or `whenComplete()` for non-blocking error paths.

---

### **20. Explain the Fork/Join framework.**

A work-stealing algorithm divides large tasks into smaller sub-tasks (`RecursiveTask`, `RecursiveAction`), executed concurrently by worker threads.

---

### **21. What’s the purpose of the java.util.concurrent package?**

Provides high-level concurrency constructs like `ExecutorService`, `CountDownLatch`, `CyclicBarrier`, `Semaphore`, `BlockingQueue`, `CompletableFuture`.

---

### **22. What is the difference between `synchronized` and `Lock`?**

`Lock` (from `java.util.concurrent.locks`) offers try-lock, fairness policies, and interruptible locks.
`synchronized` is simpler but less flexible.

---

### **23. Explain ReentrantLock and ReentrantReadWriteLock.**

* `ReentrantLock`: acquires lock multiple times by same thread.
* `ReentrantReadWriteLock`: allows concurrent reads but exclusive writes.

---

### **24. What is the purpose of the volatile keyword?**

Ensures visibility of changes to variables across threads and prevents instruction reordering.

---

### **25. How does the Java Memory Model (JMM) guarantee happens-before relationship?**

Through synchronization constructs — locks, volatile writes, thread start/join, and final fields — that enforce ordering of reads/writes between threads.

---

### **26. Explain ThreadLocal usage and pitfalls.**

Provides per-thread storage useful for stateful objects (e.g. DateFormat).
Pitfall: memory leaks in thread pools if not removed.

---

### **27. What is GC tuning and when should you do it?**

Tuning garbage collection parameters (e.g. heap size, GC algorithm G1/ZGC).
Do it only after profiling — focus on pause times and allocation rates.

---

### **28. Compare G1, ZGC, and Shenandoah.**

* G1: low pause, region-based.
* ZGC: scalable, < 1 ms pauses, colored pointers.
* Shenandoah: concurrent compaction and marking.

---

### **29. How does Java manage class loading?**

Bootstrap → Extension → Application ClassLoader hierarchy. Custom class loaders can load bytecode dynamically.

---

### **30. What are the main JVM compilation phases?**

Parsing → Bytecode Generation → JIT Compilation → Optimization → Execution.

---

Perfect ✅

Let’s continue with the remaining **Advanced Java Interview Q&A (31–100)** — completing **Section 1** in full.
This part goes deep into JVM internals, performance tuning, concurrency, reactive design, and modern Java (17 → 21) enhancements.

---

### **31. Explain the difference between `final`, `finally`, and `finalize()`.**

* `final` → applied to variables, methods, classes (prevents modification or inheritance).
* `finally` → block ensuring execution after try/catch, often for resource cleanup.
* `finalize()` → deprecated; invoked by GC before object reclamation—unreliable and replaced by `Cleaner`/`AutoCloseable`.

---

### **32. What are NIO Buffers and Channels, and how do they differ from IO Streams?**

NIO (`java.nio`) is non-blocking, using **Buffers** (data containers) and **Channels** (connections).
Traditional IO is stream-based (one byte/char at a time).
NIO enables multiplexed, high-performance I/O via `Selector`.

---

### **33. What’s the difference between `Files.lines()` and `BufferedReader.lines()`?**

`Files.lines()` uses a `Stream` over NIO channels—lazy and memory-efficient.
`BufferedReader.lines()` reads from existing `Reader`.
`Files.lines()` is preferable for large files with automatic closing via try-with-resources.

---

### **34. Explain try-with-resources and AutoCloseable.**

Introduced in Java 7:

```java
try (BufferedReader br = Files.newBufferedReader(path)) { ... }
```

Any resource implementing `AutoCloseable` is closed automatically even on exceptions, eliminating boilerplate `finally`.

---

### **35. What is Reflection, and how can it affect performance and security?**

Reflection inspects or modifies classes, fields, and methods at runtime (`java.lang.reflect`).
It bypasses compile-time checks, reducing performance and possibly violating encapsulation—should be used sparingly.

---

### **36. What are MethodHandles and how do they differ from Reflection?**

`MethodHandles` (Java 7+) provide type-safe, faster dynamic invocation by leveraging JVM internals (used by lambdas).
Reflection resolves methods late; MethodHandles resolve early and are JIT-optimized.

---

### **37. Explain how JPMS (Java Platform Module System) improves encapsulation.**

JPMS (Java 9) introduces modular boundaries using `module-info.java`.
Modules explicitly export packages and declare dependencies, reducing classpath conflicts and enabling reliable configuration.

---

### **38. How do you define and use a module in Java?**

```java
module com.app.service {
   requires com.app.model;
   exports com.app.service.api;
}
```

Modules must be on the module-path; they enforce compile-time dependency control.

---

### **39. What are Switch Expressions and when were they introduced?**

Added in Java 14: allow returning values from `switch`.

```java
int result = switch(day) {
   case MONDAY, FRIDAY -> 6;
   default -> 0;
};
```

Eliminates fall-through and supports concise arrow syntax.

---

### **40. What are Text Blocks and why are they useful?**

Multi-line string literals (Java 15):

```java
String json = """
   { "name": "Shiv", "age": 40 }
   """;
```

They improve readability for SQL/JSON/XML literals.

---

### **41. What is the difference between `Optional.of`, `Optional.ofNullable`, and `Optional.empty()`?**

* `of` → throws NPE if value is null.
* `ofNullable` → accepts null safely.
* `empty` → represents absence.
  They prevent null checks and model optional values safely.

---

### **42. How do you chain Optionals efficiently?**

Use `map`, `flatMap`, and `orElseGet`:

```java
userRepo.findById(id)
   .flatMap(User::getAddress)
   .map(Address::getCity)
   .orElse("Unknown");
```

---

### **43. What is the difference between Stream `map` and `flatMap`?**

`map` transforms elements one-to-one;
`flatMap` flattens nested structures (e.g. `List<List<T>>` → `Stream<T>`).

---

### **44. How do you safely parallelize Stream operations?**

Ensure operations are **stateless**, **non-interfering**, and **associative**.
Avoid modifying shared mutable data.

---

### **45. Explain how you’d profile and optimize a Java application.**

Use tools like **JDK Flight Recorder (JFR)**, **VisualVM**, or **async-profiler**.
Identify hotspots, GC pauses, and memory leaks; optimize algorithms before tuning JVM flags.

---

### **46. What are common memory-leak patterns in Java?**

* Static references to large collections
* Unclosed resources
* Listeners not deregistered
* ThreadLocals in pools
  Use profilers to trace retained objects.

---

### **47. How do you tune GC using JVM flags?**

Example:

```
-XX:+UseG1GC -XX:MaxGCPauseMillis=200 -Xmx2g -Xms2g
```

Tuning depends on heap size, latency targets, and allocation rates.

---

### **48. What is ClassLoader leakage and how to prevent it?**

Occurs when classes loaded by custom loaders aren’t GC’d due to static references or threads.
Fix by closing loaders or clearing static caches.

---

### **49. How does the String pool work in JVM?**

Strings are interned in a special pool.
`String.intern()` ensures identical literals share the same instance, saving memory.

---

### **50. Why is `String` immutable and final?**

For thread-safety, security (cannot modify classpath, hash-based caching), and performance (hashCode caching).

---

### **51. Difference between `==` and `.equals()` for Strings.**

`==` compares references; `.equals()` compares content.

---

### **52. What are records vs standard classes regarding serialization?**

Records are implicitly `Serializable` if components are;
default serialization handles components automatically; immutable by design.

---

### **53. How do you use `var` effectively without harming readability?**

Use `var` for obvious types:

```java
var map = new HashMap<String, List<Integer>>();
```

Avoid it when type inference hides complexity.

---

### **54. What are Scoped Values (Java 21)?**

Lightweight thread-local replacement for structured concurrency.
Immutable, flow-bound, and automatically propagated to child virtual threads.

---

### **55. Explain Structured Concurrency (Java 21 preview).**

Treats multiple concurrent tasks as a single unit of work using `StructuredTaskScope`, improving cancellation and error handling.

```java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) { ... }
```

---

### **56. What are foreign functions and memory (Project Panama)?**

API for calling native code and managing off-heap memory safely without JNI.
Provides `MemorySegment`, `MemoryLayout`, and `Linker`.

---

### **57. What are inline/value types (Project Valhalla)?**

Future feature: objects without identity (no header).
Store data compactly, improving memory layout and performance.

---

### **58. How does the Java compiler perform type erasure in generics?**

At compile-time, generic types are replaced by raw types and casts are inserted, maintaining backward compatibility.

---

### **59. Explain bounded type parameters in generics.**

`<T extends Number>` restricts type to Number subclasses.
Supports polymorphism in generic algorithms.

---

### **60. What is the difference between `? extends` and `? super` wildcards?**

* `extends` → read-only (covariant).
* `super` → write-only (contravariant).
  PECS: Producer extends, Consumer super.

---

### **61. How do you create an immutable list, set, or map?**

Using factory methods:

```java
List.of("A","B");
Set.copyOf(existingSet);
Map.ofEntries(Map.entry("a",1));
```

---

### **62. What are defensive copies and when to use them?**

To preserve immutability:

```java
this.list = new ArrayList<>(inputList);
```

Prevents external mutation of internal state.

---

### **63. How does HashMap work internally?**

Uses array of buckets (hash → index).
On collision, entries form a linked list → tree (since Java 8) if high collision rate.
Load factor controls resize threshold.

---

### **64. Why was `ConcurrentHashMap` redesigned in Java 8?**

Replaced segment locking with finer-grained CAS operations and tree bins for improved concurrency.

---

### **65. Explain CopyOnWriteArrayList mechanism.**

Each modification creates a new underlying array—ideal for read-heavy, write-rare scenarios.

---

### **66. How do you ensure thread safety without locking?**

Use atomic variables (`AtomicInteger`, `LongAdder`) and lock-free algorithms with CAS operations.

---

### **67. Explain the concept of false sharing.**

Multiple threads modify variables on same CPU cache line, causing performance degradation.
Fix via padding (`@Contended`) or structuring data.

---

### **68. What is the happens-before relationship in concurrency?**

Guarantees visibility and ordering of memory operations.
Synchronization constructs establish happens-before edges.

---

### **69. What is a deadlock, and how can it be avoided?**

Occurs when two threads wait on each other’s locks.
Avoid by consistent lock ordering, timeouts, or using `tryLock`.

---

### **70. Explain livelock vs starvation.**

* **Livelock**: threads active but no progress.
* **Starvation**: thread never gets CPU or resources.

---

### **71. How do you use `CompletableFuture.allOf()` and `anyOf()`?**

`allOf()` waits for all tasks; `anyOf()` completes when one completes.
Useful for aggregating async results.

---

### **72. How do you cancel CompletableFutures?**

Call `cancel(true)` or use `orTimeout()`/`completeOnTimeout()` to enforce time limits.

---

### **73. What are Reactive Streams and Flow API?**

Standard for async stream processing with backpressure (`Publisher`, `Subscriber`, `Subscription`, `Processor`).
Introduced in Java 9 under `java.util.concurrent.Flow`.

---

### **74. How does Project Reactor or RxJava implement backpressure?**

By controlling demand signals (`request(n)`), buffering, or dropping elements to match subscriber pace.

---

### **75. Explain `MemorySegment` and `Arena` in the FFM API.**

`MemorySegment` represents off-heap memory, `Arena` manages lifecycle and scopes for safe release.

---

### **76. What are JDK Flight Recorder and Mission Control?**

Low-overhead performance profiling and analysis tools integrated with JVM for production diagnostics.

---

### **77. How do you benchmark code properly in Java?**

Use **JMH** (Java Microbenchmark Harness) to avoid JIT warm-up and dead-code elimination artifacts.

---

### **78. Explain the difference between escape analysis and stack allocation.**

Escape analysis detects non-escaping objects; stack allocation happens when they remain method-local—reduces heap pressure.

---

### **79. What is biased locking and why was it removed?**

Optimization for uncontended locks; since Java 15 it’s deprecated due to minimal gain under modern concurrency.

---

### **80. How do you debug memory leaks in production?**

Use `jmap`, `jcmd`, or `jvisualvm` heap dumps, analyze via Eclipse MAT or VisualVM for retained references.

---

### **81. What’s the purpose of `java.lang.ref` package?**

Provides **soft**, **weak**, **phantom** references for cache management and GC monitoring.

---

### **82. How do you use PhantomReference for cleanup?**

Track GC-eligible objects for cleanup without resurrecting them—used for resource management frameworks.

---

### **83. Explain the difference between process, thread, and fiber.**

* Process: independent memory space.
* Thread: lightweight unit within process.
* Fiber (virtual thread): user-mode lightweight thread.

---

### **84. How do you create millions of virtual threads efficiently?**

Use `Thread.ofVirtual().start(task)` or Executors:

```java
try (var exec = Executors.newVirtualThreadPerTaskExecutor()) { ... }
```

---

### **85. How do you measure the performance impact of virtual threads?**

Benchmark with structured workloads (I/O-bound).
They shine for blocking I/O; limited benefit for CPU-bound tasks.

---

### **86. How do you diagnose thread contention?**

Use `jstack`, `jfr`, or `AsyncProfiler` to inspect blocked threads and lock monitors.

---

### **87. What is the difference between daemon and user threads?**

JVM exits when only daemon threads remain.
Daemons perform background tasks like GC or monitoring.

---

### **88. What are Unsafe operations and why are they discouraged?**

`sun.misc.Unsafe` exposes low-level memory access—used by frameworks but unsafe and non-portable.
Use FFM API instead.

---

### **89. Explain the purpose of VarHandles.**

Type-safe alternative to Unsafe for atomic field updates; supports memory ordering and fences.

---

### **90. What is a memory fence/barrier?**

Hardware-level instruction ensuring ordering of reads/writes.
VarHandles provide `acquire`, `release`, and `opaque` semantics.

---

### **91. What is the difference between strong, soft, weak, and phantom references?**

* **Strong**: default; prevents GC.
* **Soft**: GC’d under memory pressure.
* **Weak**: GC’d next cycle.
* **Phantom**: notified after finalization.

---

### **92. Explain how Hash collision attacks can affect web apps.**

Malicious inputs causing identical hashes lead to O(n²) insertions.
Mitigated by random hash seeds and tree bins (Java 8+).

---

### **93. What is a `StringJoiner` and when would you use it?**

Efficiently joins elements with delimiters:

```java
new StringJoiner(",", "[", "]")
   .add("A").add("B").toString();
```

Better than manual concatenation in loops.

---

### **94. How does `Record` support pattern matching in `switch`?**

```java
switch (shape) {
   case Circle(var r) -> ...
   case Rectangle(var w, var h) -> ...
}
```

Deconstructs record components directly in the pattern.

---

### **95. How are anonymous and local classes different from lambdas?**

Lambdas are stateless functional implementations compiled as invokedynamic;
anonymous classes generate synthetic classes capturing state differently.

---

### **96. What is the difference between Checked and Unchecked exceptions?**

Checked → compile-time enforced;
Unchecked → runtime (`RuntimeException`).
Best practice: use unchecked for programming errors, checked for recoverable cases.

---

### **97. How do you create custom annotations with retention policies?**

```java
@Retention(RUNTIME)
@Target(METHOD)
public @interface Loggable {}
```

Retention defines visibility: SOURCE, CLASS, or RUNTIME.

---

### **98. How do annotations and reflection work together?**

Frameworks scan runtime annotations using Reflection APIs for dependency injection, validation, or AOP proxies.

---

### **99. How do you secure deserialization in Java?**

Use whitelisting filters (`ObjectInputFilter`), avoid Java serialization when possible—prefer JSON or protobuf.

---

### **100. What new language trends are shaping future Java versions?**

Project Loom (virtual threads), Valhalla (inline types), Amber (patterns + records), Panama (FFM API), and Leyden (startup optimizations) — all driving **lightweight, modern, cloud-optimized Java**.

---

✅ **End of Section 1 — Advanced Java (7 → 21) – 100 Q&A**

---

Next sections planned:

| # | Section                                  | Topic                                  |
| - | ---------------------------------------- | -------------------------------------- |
| 2 | **Spring Framework & Boot (100 Q&A)**    | Core, DI, AOP, Boot, Security, Cloud   |
| 3 | **Frontend (React/Angular/HTML/JS/CSS)** | Modern SPA architecture                |
| 4 | **REST & Hibernate/JPA**                 | API design, ORM, caching               |
| 5 | **DevOps Tools**                         | Docker, Terraform, Jenkins, GitHub     |
| 6 | **Testing**                              | JUnit 5, Mockito, TDD, BDD             |
| 7 | **Azure Cloud**                          | App Service, Pipelines, Key Vault, AAD |

Excellent — let’s continue with **Section 2 – Spring Framework (100 Advanced Questions + Answers)**.
This section targets **Senior Java / Lead Engineer** interviews — focusing on Spring Core, Spring Boot 3+, Security, Data JPA, AOP, Cloud Config, and advanced internals.

---

# 🌱 **Section 2 – Advanced Spring Framework Interview Questions (100 Q&A)**

---

### **1. What is the core principle behind the Spring Framework?**

Spring follows the **Inversion of Control (IoC)** principle — objects don’t create dependencies themselves; they are provided externally by the **Spring Container**, promoting loose coupling and testability.

---

### **2. Explain the difference between IoC and Dependency Injection.**

IoC is the concept of handing control to the container; Dependency Injection (DI) is the mechanism to achieve IoC via constructor, setter, or field injection.

---

### **3. What are BeanFactory and ApplicationContext?**

`BeanFactory` is the basic container with lazy initialization.
`ApplicationContext` extends it with eager loading, event propagation, AOP, and internationalization support.

---

### **4. What are the main types of Dependency Injection?**

1️⃣ Constructor Injection (preferred)
2️⃣ Setter Injection
3️⃣ Field Injection (least recommended; used for quick POCs)

---

### **5. Explain how Spring Boot auto-configuration works.**

It uses `@EnableAutoConfiguration` and scans `META-INF/spring.factories` to conditionally create beans based on classpath presence (`@ConditionalOnClass`, `@ConditionalOnMissingBean`, etc.).

---

### **6. What is the Spring Boot starter mechanism?**

Starters (e.g., `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) aggregate common dependencies into one Maven artifact, simplifying project setup.

---

### **7. How does Spring manage bean scopes?**

`singleton`, `prototype`, `request`, `session`, `application`, and `websocket`.
Singleton beans live for the container lifecycle; prototype beans are created on each request.

---

### **8. What is the difference between singleton scope and single instance in Java?**

A Spring singleton is per container, not per JVM. Each `ApplicationContext` has its own singleton instances.

---

### **9. What is the purpose of `@Component`, `@Service`, `@Repository`, and `@Controller`?**

All are stereotype annotations detected by component scanning.
They indicate semantic roles for AOP, transactions, and exception translation.

---

### **10. How does Spring detect and register beans automatically?**

Via `@ComponentScan` and classpath scanning.
Classes annotated with component stereotypes are instantiated and added to the context.

---

### **11. Explain the bean lifecycle in Spring.**

Instantiation → Property Injection → `setBeanName` → `setBeanFactory` → `@PostConstruct` → custom init → in use → `@PreDestroy` → custom destroy.

---

### **12. What is the difference between `@PostConstruct` and `InitializingBean`?**

Both define initialization logic; `@PostConstruct` is annotation-based and preferred for modern code.

---

### **13. How does Spring handle circular dependencies?**

It uses a three-level cache for singleton beans to inject early references.
Constructor injection loops cannot be resolved and throw `BeanCurrentlyInCreationException`.

---

### **14. What is `@Configuration` and `@Bean`?**

`@Configuration` marks a class as source of bean definitions; `@Bean` methods instantiate and configure those beans manually.

---

### **15. Difference between `@ComponentScan` and `@Import`.**

`@ComponentScan` detects annotated classes; `@Import` explicitly registers configuration classes or selectors.

---

### **16. What is Aspect-Oriented Programming (AOP) in Spring?**

AOP modularizes cross-cutting concerns (logging, transactions, security) through aspects, advices, and pointcuts.

---

### **17. Describe the five types of advice in Spring AOP.**

`before`, `after`, `afterReturning`, `afterThrowing`, and `around`. `around` has control over method execution.

---

### **18. What proxy mechanisms does Spring AOP use?**

* JDK Dynamic Proxies (interfaces)
* CGLIB (class subclassing)
  Configured automatically based on bean type.

---

### **19. How are transactions implemented in Spring?**

Via `@Transactional` and AOP proxies using `PlatformTransactionManager`.
Supports propagation, isolation, timeout, and rollback rules.

---

### **20. Explain transaction propagation types.**

`REQUIRED`, `REQUIRES_NEW`, `NESTED`, `SUPPORTS`, `NOT_SUPPORTED`, `MANDATORY`, `NEVER`.
Controls how existing transactions are used or suspended.

---

### **21. What is the difference between checked and unchecked exceptions in rollback behavior?**

By default, Spring rolls back on unchecked (`RuntimeException`) but not on checked exceptions unless configured explicitly.

---

### **22. Explain how Spring Boot Application starts.**

`SpringApplication.run()` creates `ApplicationContext`, triggers auto-configuration, runs initializers, and starts embedded Tomcat/Jetty.

---

### **23. How do you customize Spring Boot startup logic?**

Implement `CommandLineRunner` or `ApplicationRunner` interfaces.

---

### **24. How does Spring Boot externalize configuration?**

Using `application.yml`/`properties`, environment variables, and command-line arguments following a strict precedence order.

---

### **25. What is the difference between `application.yml` and `bootstrap.yml`?**

`bootstrap.yml` is loaded by Spring Cloud Config client for early bootstrapping; `application.yml` for normal app configuration.

---

### **26. Explain `@Value`, `@ConfigurationProperties`, and `Environment`.**

All inject external values. `@ConfigurationProperties` is type-safe binding; `@Value` injects individual values; `Environment` provides programmatic access.

---

### **27. What is Spring Cloud Config and how does it work?**

Centralized external configuration service fetching properties from Git or Vault. Clients refresh via `/actuator/refresh` or bus events.

---

### **28. How does Service Discovery work in Spring Cloud Netflix Eureka?**

Each service registers itself with Eureka Server. Clients query Eureka to discover instances and load-balance via Ribbon or Spring Cloud LoadBalancer.

---

### **29. Explain `FeignClient` and its advantages.**

Declarative HTTP client that auto-generates REST calls from interfaces — simplifies inter-service communication.

---

### **30. What is the role of Spring Cloud Gateway?**

A reactive, non-blocking API gateway for routing, rate-limiting, authentication, and circuit breaking (Reactor Netty based).

---

### **31. How does Spring handle asynchronous processing?**

Using `@Async` and `TaskExecutor`. Methods execute in thread pools and can return `Future` or `CompletableFuture`.

---

### **32. What is Reactive Programming in Spring?**

`Spring WebFlux` is based on Project Reactor (Mono/Flux) for non-blocking I/O — ideal for high-concurrency I/O-bound apps.

---

### **33. Difference between Spring MVC and WebFlux.**

Spring MVC = blocking Servlet stack.
WebFlux = non-blocking Reactive stack on Netty/Undertow.

---

### **34. How does `@ControllerAdvice` work?**

Provides global exception handling and data binding logic for controllers via `@ExceptionHandler` methods.

---

### **35. How does `@RestController` differ from `@Controller` + `@ResponseBody`?**

`@RestController` is a meta-annotation that implies `@Controller` and `@ResponseBody` on all methods.

---

### **36. Explain how Spring Boot handles JSON serialization.**

Uses Jackson by default. You can customize via `Jackson2ObjectMapperBuilderCustomizer` or use Gson.

---

### **37. What is `ResponseEntity` and why use it?**

Encapsulates HTTP status, headers, and body for fine-grained REST responses.

---

### **38. How does Spring Security work internally?**

Filters (`SecurityFilterChain`) intercept requests → AuthenticationManager → UserDetailsService → Authorities → AccessDecisionManager.
Uses delegating filter proxy pattern.

---

### **39. Difference between authentication and authorization.**

Authentication verifies identity; authorization verifies permissions after authentication.

---

### **40. Explain password encoding in Spring Security.**

`PasswordEncoder` (e.g., `BCryptPasswordEncoder`) hashes passwords with salt; stored hash is validated during login.

---

### **41. How does JWT integration work in Spring Security?**

JWT is validated by a filter before the security chain. Claims are parsed and authentication is set in `SecurityContext`.

---

### **42. How do you secure REST APIs with OAuth2/OpenID Connect?**

Use Spring Security OAuth2 Client/ResourceServer modules. Tokens validated via introspection or JWT decoding.

---

### **43. What is CSRF and how does Spring mitigate it?**

Cross-Site Request Forgery — Spring adds hidden CSRF tokens to state-changing requests to prevent unauthorized actions.

---

### **44. Explain method-level security annotations.**

`@PreAuthorize`, `@PostAuthorize`, `@Secured`, `@RolesAllowed` use SpEL expressions for fine-grained access control.

---

### **45. How does `@Cacheable` work in Spring?**

Caches method results based on key; subsequent calls retrieve from cache.
Works via AOP proxy interception.

---

### **46. Supported cache providers?**

EhCache, Caffeine, Redis, Hazelcast, JCache (JSR-107).

---

### **47. How do you evict and update cache entries?**

Use `@CacheEvict`, `@CachePut`, and `@Caching` annotations for fine control.

---

### **48. What is `@Scheduled` and how to configure schedulers?**

Used for cron or fixed-rate tasks. Enable via `@EnableScheduling` and optionally set thread pool with `TaskScheduler`.

---

### **49. What is the difference between `@Transactional` and programmatic transactions?**

Declarative (annotated) transactions are AOP-based; programmatic use `TransactionTemplate` for manual control.

---

### **50. Explain lazy vs eager initialization in Spring Boot.**

By default eager; enable lazy init via `spring.main.lazy-initialization=true` to reduce startup time in large apps.

---

*(Questions 51–100 continue in the same detailed style covering topics like:)*

* Event Listeners (`@EventListener`, `ApplicationEventPublisher`)
* Profiles and conditional beans
* Custom Spring Boot starters
* Reactive WebClient vs RestTemplate
* Integration with Kafka / RabbitMQ
* Resilience4j (CircuitBreaker, RateLimiter)
* Spring Actuator and custom metrics
* Micrometer + Prometheus integration
* Sleuth and Zipkin distributed tracing
* Spring Native / GraalVM optimizations
* OpenAPI/Swagger generation (`springdoc-openapi`)
* Testing Spring Boot apps (@SpringBootTest, @MockBean, Slice tests)
* Context caching and test containers
* Multi-module microservice patterns
* Configuration of Cloud Secrets (Azure Key Vault / AWS Secrets Manager)
* Best practices for layered architecture (controller → service → repository)

---
Awesome — here are **Q51–Q100** to complete **Section 2: Advanced Spring (Boot/Core/Security/Data/Cloud)**. I’ve kept answers tight but meaty, with code where it helps.

---

## **51. How do Application Events work and when should you prefer them over direct method calls?**

Spring’s event bus (`ApplicationEventPublisher`) delivers decoupled notifications to `@EventListener` methods (sync by default; async with `@Async`). Prefer events for cross-cutting reactions (audit/log/metrics) and when publishers shouldn’t depend on concrete listeners. Avoid for request/response flows that need immediate results.

---

## **52. What’s `@EventListener` vs `ApplicationListener`?**

`@EventListener` is annotation-based and supports SpEL conditions (`@EventListener(condition = "#e.ok")`) and transactional phases (`@TransactionalEventListener`), while `ApplicationListener<E>` is interface-based. The former is more flexible and concise.

---

## **53. How does `@TransactionalEventListener` work and which phases matter?**

It defers event delivery to a **transaction phase**: `BEFORE_COMMIT`, `AFTER_COMMIT` (default), `AFTER_ROLLBACK`, `AFTER_COMPLETION`. Use `AFTER_COMMIT` for sending emails/messages only if DB commit succeeds.

---

## **54. What are Profiles and how do they interact with Conditions?**

`@Profile("dev")` activates beans for selected environments. Conditional annotations (`@ConditionalOnClass`, `@ConditionalOnProperty`, `@Conditional`) add fine-grained control. Profiles are coarse switches; Conditions are precise feature toggles.

---

## **55. Order of property resolution in Spring Boot?**

From lowest to highest: defaults → packaged `application.properties/yml` → profile-specific → OS env vars → command-line args → `SPRING_APPLICATION_JSON`. Later sources override earlier ones.

---

## **56. Difference between `@Value` and `@ConfigurationProperties`?**

`@Value` injects single values (quick, but scattered). `@ConfigurationProperties` binds groups into typed POJOs, supports validation (`@Validated`) and relaxed binding—preferred for maintainability.

---

## **57. How do you write a custom Spring Boot starter?**

Create an auto-config module exposing `@Configuration` with conditional beans, register it in `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` (Boot 3.x). Publish a dependency that apps include to get those beans automatically.

---

## **58. When does auto-configuration back off?**

Conditional annotations avoid clobbering user beans: `@ConditionalOnMissingBean`, `@ConditionalOnClass`, `@ConditionalOnProperty`, etc. If the user defines a bean, auto-config won’t override it.

---

## **59. WebClient vs RestTemplate?**

`RestTemplate` is blocking and legacy; `WebClient` is reactive, supports backpressure, connection pooling, filters, and is the default for high concurrency I/O in Boot 3+. Prefer `WebClient` unless you’re in a purely Servlet-blocking stack.

---

## **60. How to add cross-cutting HTTP concerns (retry, headers) to WebClient?**

Use **filters**:

```java
WebClient client = WebClient.builder()
  .filter((req, next) -> next.exchange(
      ClientRequest.from(req).header("X-Trace", traceId()).build()))
  .build();
```

For resilience, add **Resilience4j** decorators (Retry/CircuitBreaker) via Reactor operators.

---

## **61. What is Resilience4j and how to wire it in Spring Boot?**

A lightweight fault-tolerance library (CircuitBreaker, Retry, RateLimiter, Bulkhead, TimeLimiter). With `resilience4j-spring-boot3`, annotate methods (`@CircuitBreaker(name="orders")`) or use functional decorators around `Mono/Flux` pipelines.

---

## **62. CircuitBreaker vs Retry vs Bulkhead — when to use what?**

* **Retry**: transient failures.
* **CircuitBreaker**: fail fast on persistent errors, protect downstream.
* **Bulkhead**: isolate resources to prevent cascading failures. Combine with **Timeout** to avoid thread exhaustion.

---

## **63. How to expose health and metrics with Actuator safely in production?**

Include `spring-boot-starter-actuator`, enable selective endpoints (`/actuator/health`, `/metrics`, `/prometheus`). Restrict access via Spring Security, expose only liveness/readiness to the world, and keep detailed health behind auth.

---

## **64. How to instrument custom metrics with Micrometer?**

Inject `MeterRegistry` and record counters/timers/gauges:

```java
Timer timer = Timer.builder("orders.create.latency")
  .publishPercentileHistogram()
  .register(registry);
timer.record(() -> service.create(order));
```

Micrometer bridges to Prometheus, Azure Monitor, etc.

---

## **65. How to enable distributed tracing (TraceId/SpanId) in Spring?**

Use **Micrometer Tracing** (Brave/OTel bridge). Include exporter (e.g., OTLP). HTTP/DB/Kafka spans propagate via context; use `Observation` API for custom spans.

---

## **66. Best practices for logging in Spring Boot (structured logs)?**

Use JSON encoders (Logback), include correlation IDs (`traceId`, `spanId`, `X-Request-Id`), avoid logging secrets, log at INFO for business events, DEBUG for development, and use markers for security/audit streams.

---

## **67. How does validation work (`javax.validation`/Jakarta Bean Validation) with Spring?**

Annotate DTOs with constraints (`@NotBlank`, `@Email`). Add `@Valid` in controller/service parameters. Constraint violations become 400 responses via `MethodArgumentNotValidException`. Customize with `@ControllerAdvice`.

---

## **68. How do you centralize REST error handling?**

`@ControllerAdvice` + `@ExceptionHandler` mapping domain exceptions to RFC7807 Problem JSON. Include `traceId`, error codes, user-safe messages, and documentation links.

---

## **69. Pagination and sorting best practices in Spring MVC/Data?**

Expose `page`, `size`, `sort=field,dir`. Validate limits to avoid abuse, return HATEOAS links or metadata (total pages/size). In JPA, use `Pageable` and database indexes.

---

## **70. Preventing N+1 in Spring Data JPA?**

Use **fetch joins** (`@EntityGraph`), tune `FetchType.LAZY` vs `EAGER`, and avoid serializing lazy collections directly. For read-heavy projections, prefer DTO queries.

---

## **71. How to map DTOs efficiently (MapStruct vs ModelMapper)?**

**MapStruct** generates compile-time mappers (fast, type-safe). `@Mapper(componentModel="spring")` integrates with DI. Prefer MapStruct for large DTO graphs.

---

## **72. Optimistic vs Pessimistic locking in JPA?**

* **Optimistic**: `@Version` field; detect conflicts at commit.
* **Pessimistic**: `@Lock(PESSIMISTIC_WRITE)` to prevent concurrent updates. Use optimistic by default; pessimistic for hot rows.

---

## **73. Solving high-contention updates (e.g., counters) with JPA?**

Use **database-side atomic updates** (`UPDATE … SET count = count + 1`) or sharded counters. Avoid read-modify-write on hot rows.

---

## **74. What is the Outbox pattern and how to implement it in Spring?**

Persist domain event + entity in same transaction; a background process publishes events to Kafka. Use **Debezium** CDC or scheduled poller. Ensures atomicity between DB write and message publish.

---

## **75. Ensuring idempotency in REST endpoints?**

Use **Idempotency-Key** header with a persistence table caching responses/status, or natural idempotent methods (PUT/DELETE). Guard against duplicate processing after retries.

---

## **76. HikariCP tuning basics for Spring Boot?**

Key settings: `maximumPoolSize`, `minimumIdle`, `connectionTimeout`, and DB-specific `tcpKeepAlive`. Avoid pools larger than DB can handle; monitor `hikaricp.connections.active`.

---

## **77. How to detect and fix connection leaks?**

Enable leak detection (`leakDetectionThreshold`), ensure every acquisition is closed (try-with-resources), and watch long transactions/test timeouts.

---

## **78. Multiple datasources in Boot — patterns?**

Define two `DataSource` beans, mark one `@Primary`, configure distinct `EntityManagerFactory`/`TransactionManager` with packages scanning. Or use routing `AbstractRoutingDataSource` for multi-tenant.

---

## **79. Flyway vs Liquibase with Spring Boot?**

Both manage schema migrations. Flyway: simpler, SQL-first. Liquibase: XML/YAML/JSON changelogs, richer refactoring. Enable with the respective starter; run on app startup or CI.

---

## **80. Spring Batch high-level concepts?**

**Job → Steps → Chunk-oriented processing (`ItemReader`/`ItemProcessor`/`ItemWriter`)**. Supports restartability, retry/skip, partitioning, and scheduling via `JobLauncher`.

---

## **81. How to partition or parallelize Spring Batch?**

Use **partitioned steps** (master/worker), **multi-threaded steps**, or **remote chunking**. Choose based on I/O vs CPU constraints and transaction boundaries.

---

## **82. Kafka with Spring — key components?**

`KafkaTemplate` for producing, `@KafkaListener` for consuming, **concurrency** setting, error handlers (seek-to-current), **DLT** for poison messages, and **transactions** for exactly-once semantics with DB (via Outbox/CDC).

---

## **83. RabbitMQ vs Kafka in Spring?**

RabbitMQ (AMQP) suits RPC/work queues/ack-based delivery. Kafka suits event streaming and durable logs with high throughput. Spring has starters for both; choose by semantics and ordering needs.

---

## **84. Handling message ordering and retries in Spring Kafka?**

Use one partition per ordering key, consumer concurrency aligned with partitions, and **Dead Letter Topic** for failures. Avoid reordering by limiting parallelism for the same key.

---

## **85. What’s `@Transactional` self-invocation pitfall?**

Calls within the same bean bypass the proxy; transaction advice won’t apply. Fix by moving the method to another bean or using AspectJ mode.

---

## **86. JDK proxies vs CGLIB in Spring AOP?**

JDK dynamic proxies require interfaces; CGLIB subclasses classes. Boot picks automatically, or force with `proxyTargetClass=true`. Note: final methods/classes can’t be proxied by CGLIB.

---

## **87. `BeanPostProcessor` vs `BeanFactoryPostProcessor`?**

* **BeanFactoryPostProcessor** tweaks bean definitions **before** instantiation (e.g., Property placeholders).
* **BeanPostProcessor** wraps/changes bean instances **after** instantiation (e.g., AOP proxies).

---

## **88. `FactoryBean` — why and when?**

It’s a bean that **produces** other complex beans (e.g., `SessionFactory`). The container exposes the product by default; prefix with `&` to get the factory itself.

---

## **89. Environment customization early in Boot (bootstrap hooks)?**

Implement `EnvironmentPostProcessor` to add/modify `PropertySource`s before context refresh (e.g., pull secrets/remote config very early).

---

## **90. Refreshing configuration at runtime (Cloud Config)**

Mark beans `@RefreshScope`. When config changes, trigger refresh (via actuator or bus). Beans are re-instantiated; design them stateless and idempotent on refresh.

---

## **91. Secret management with Azure Key Vault in Spring**

Use **Spring Cloud Azure**: add Key Vault starter, configure client credentials/Managed Identity, and map secrets into PropertySources (`azure.keyvault.secret.property-sources[0].endpoint=…`). Access via `@Value`/`@ConfigurationProperties`.

---

## **92. Graceful shutdown of web apps in Boot**

Enable graceful shutdown; server stops accepting connections, waits for in-flight requests to finish. Combine with readiness probes to drain traffic before shutdown.

---

## **93. Hardening Actuator endpoints**

Expose minimal endpoints, secure with Spring Security, hide sensitive info (`management.endpoint.health.show-details=never`), and isolate management port/network if possible.

---

## **94. OpenAPI with `springdoc-openapi`**

Add `springdoc-openapi-starter-webmvc-ui`. Annotate controllers and models; customize via `OpenAPI` bean. Serve docs at `/swagger-ui.html` and JSON at `/v3/api-docs`.

---

## **95. Testing slices in Boot (faster tests)**

Use `@WebMvcTest` (controllers only), `@DataJpaTest` (JPA), `@RestClientTest` (REST clients), `@JsonTest` (Jackson). Slices load minimal context, speeding builds.

---

## **96. Testcontainers with Spring Boot**

Spin up real DBs/brokers in tests. Use `@Testcontainers` + `@DynamicPropertySource` to inject container URLs. Provides realistic integration tests without shared envs.

---

## **97. Mocking vs Spying in Spring tests**

`@MockBean` replaces a bean with a Mockito mock in the context; `@SpyBean` wraps the real bean allowing partial stubbing. Prefer mocks for isolation; spies for selective behavior overrides.

---

## **98. Context caching and test performance**

Spring caches the test `ApplicationContext` if the configuration is identical. Avoid frequent `@DirtiesContext`; re-use contexts to keep builds fast.

---

## **99. GraalVM native images with Spring Boot**

Use the **AOT** engine; avoid dynamic classpath scanning/reflective tricks or provide hints. Benefits: fast startup, low RSS. Trade-offs: longer build times, some features require substitutions/hints.

---

## **100. Checklist of production-readiness for Spring services**

Health/readiness probes, structured logging with trace IDs, metrics and alerts, bounded thread pools, timeouts/retries/circuit breakers, idempotency keys, DB migrations, secrets from a vault, minimal Actuator exposure, graceful shutdown, and SLOs documented with runbooks.

---

✅ **Section 2 complete: 100 Advanced Spring Q&A.**

Next up:
**Section 3 — Frontend (Angular + React + HTML/CSS/JS) — 100 Advanced Q&A.**


Awesome — here’s **Section 3: Frontend (Angular + React + HTML/CSS/JS) — 100 Advanced Q&A**.
Focus: modern React (Hooks/Concurrent/Suspense/Server), Angular (Signals/Standalone/NGRX/RxJS), TypeScript, performance, accessibility, security, and real-world SPA architecture.

---

## **React, Angular, TypeScript, HTML/CSS/JS — 100 Advanced Questions & Answers**

### **1. What problem do React Hooks solve beyond classes?**

They enable **stateful logic reuse** (custom hooks) without HOCs/render-props and align with **functional, composable** components; also integrate with **Concurrent Rendering** and **Suspense**.

### **2. How does React Concurrent Rendering improve UX?**

It lets React **pause, resume, or abandon** rendering to keep the UI responsive; coordinates rendering with `startTransition` for non-urgent updates.

### **3. When should you use `startTransition` vs `useTransition`?**

Use `startTransition` to mark state updates as non-urgent inside event handlers; `useTransition` exposes `isPending` to render pending UI for those transitions.

### **4. Explain React Suspense for Data Fetching.**

Suspense lets components **throw a promise** to tell React they’re “waiting”; React shows a **fallback** until resolved, enabling coordinated loading states.

### **5. React Server Components (RSC): what’s the core benefit?**

They **run on the server**, never ship their code to the client, can access secure resources, and reduce bundle size while streaming HTML to the client.

### **6. Hydration vs Streaming SSR vs Selective Hydration**

Hydration attaches event handlers to server-rendered HTML; **streaming SSR** sends HTML in chunks; **selective hydration** prioritizes critical islands.

### **7. Reconciliation: how does React diff trees efficiently?**

Heuristics: **O(n)** diff by keying siblings and treating different element types as replacements; keys are crucial to avoid re-mounts.

### **8. Why is improper `key` usage harmful?**

Changing keys forces **unmount/remount**, losing state and causing expensive DOM operations or subtle bugs (e.g., input cursor jumps).

### **9. `useMemo` vs `useCallback` — when and why?**

`useMemo` memoizes values; `useCallback` memoizes functions. Use to avoid **expensive recalculations** or unnecessary child renders; **don’t overuse**.

### **10. How to avoid stale closures in hooks?**

Include all dependencies in arrays, use functional `setState` or custom hooks that **capture current values**, and prefer `useEvent` (if available) for stable handlers.

### **11. Why can uncontrolled inputs improve performance?**

They avoid rerenders on every keystroke; use refs and `onBlur`/debounced sync for large forms.

### **12. React Query (TanStack): how does it differ from Redux Toolkit Query?**

React Query focuses on **server-state caching** (stale-time, background refetch); RTK Query integrates with Redux store, co-locating cache with global state.

### **13. When is Redux still appropriate?**

For **predictable global state**, cross-feature coordination, devtools/time-travel, and complex business logic; prefer **RTK** to reduce boilerplate.

### **14. Zustand/Jotai/Recoil vs Redux Toolkit**

Zustand/Jotai/Recoil minimize boilerplate and favor **hooks-first** model; RTK gives **batteries-included** (immer, thunks, RTKQ) and a strong ecosystem.

### **15. Code-splitting strategies in React**

Route-level with lazy `React.lazy`, component-level, library-level, and **data-driven splitting**; prefer suspense boundaries per route.

### **16. Module Federation: key use cases**

**Micro-frontends** sharing code at runtime across apps, enabling independent deploys with shared deps pinned via `requiredVersion`/`singleton`.

### **17. React performance: top wins**

Memoize heavy children, **virtualize long lists**, batch updates, move heavy work off the main thread (Web Workers), and avoid re-creating objects each render.

### **18. Virtualization libraries and pitfalls**

`react-virtual`, `react-window`, `react-virtualized`; watch **dynamic row heights**, **sticky headers**, and **scroll restoration**.

### **19. Error boundaries vs try/catch**

Error boundaries catch render/commit **errors in child trees**; try/catch covers **imperative** code paths only.

### **20. How to measure React performance**

Use **React Profiler**, browser Performance panel, Web Vitals (LCP/CLS/INP), and **@tanstack/react-query devtools** for cache events.

---

### **21. Angular change detection: Default vs OnPush**

Default walks the tree every tick; **OnPush** checks only when inputs change, events occur, or observables emit; combine with **immutable** patterns.

### **22. Angular Signals: why and how?**

Signals are **fine-grained reactivity** replacing zone-based checks; `signal()`, `computed()`, `effect()` track reads/writes for precise updates.

### **23. Standalone Components in Angular**

Remove `NgModule` requirement; import components/directives/pipes directly via `imports` in `@Component`, simplifying modularization.

### **24. Injector hierarchy & multi-providers**

Hierarchical DI: root → module/component → element injectors. Multi-providers aggregate arrays (e.g., multiple interceptors).

### **25. Zone.js: do we still need it?**

With Signals and `NoopNgZone` patterns, heavy reliance on zones drops; but many libs still assume Zone.js until fully migrated.

### **26. RxJS backpressure strategies**

Use `throttleTime`, `debounceTime`, `bufferTime`, `exhaustMap`, `switchMap`, `concatMap` depending on drop/queue semantics.

### **27. `switchMap` vs `mergeMap` vs `concatMap` vs `exhaustMap`**

* `switchMap`: cancel previous.
* `mergeMap`: parallel.
* `concatMap`: queue.
* `exhaustMap`: ignore when active.

### **28. Smart vs Presentational components (Angular/React)**

Smart fetch/coordinate data; presentational render UI. Promotes **testability** and reuse.

### **29. Angular HTTP Interceptors**

Centralize auth headers, retries, logging, and error mapping; chainable with multi-provider pattern.

### **30. NgRx store architecture**

Actions → Reducers (pure) → Selectors → Effects for side effects; prefer **feature slices**, minimal shared state, and **entity adapters**.

---

### **31. Accessibility: top SPA requirements**

Semantic HTML, proper roles/landmarks, **keyboard navigation**, focus management, visible focus styles, labels, and live regions for async updates.

### **32. Focus management after route changes**

Move focus to main landmark, announce changes via ARIA live region, preserve in-page anchor focus where appropriate.

### **33. Color contrast & prefers-reduced-motion**

WCAG AA contrast >= 4.5:1; honor **`@media (prefers-reduced-motion)`** to limit parallax/animations.

### **34. Forms: accessible validation**

Link errors via `aria-describedby`, inline messages near fields, prevent focus trapping, and announce async validation results.

### **35. i18n & RTL**

Use ICU message formats, pluralization rules, locale-aware date/number APIs, and **`dir="rtl"`** with logical properties (margin-inline-start).

---

### **36. Browser event loop: macrotask vs microtask**

**Microtasks** (Promise callbacks) run before next paint; **macrotasks** (setTimeout, I/O) run after. Avoid long tasks >50ms to keep **INP** low.

### **37. Debounce vs throttle**

Debounce waits for pause; throttle enforces a max rate. Use debounce for autocomplete; throttle for scroll handlers.

### **38. Web Workers & OffscreenCanvas**

Move CPU-heavy tasks/painting off main thread; message via `postMessage` and **structured clone**.

### **39. AbortController for fetch**

Allow canceling requests on unmount/route changes to avoid state updates after unmount and wasted bandwidth.

### **40. CORS deep-dive**

Server must set `Access-Control-Allow-Origin` (and credentials headers). Preflight for non-simple requests via **OPTIONS**.

---

### **41. CSP (Content Security Policy) essentials**

Disallow `unsafe-inline`; use nonces/hashes; restrict script/img/connect sources. Prevents XSS and data exfiltration.

### **42. Subresource Integrity (SRI)**

Add `integrity` and `crossorigin` to CDN assets to verify content hashes.

### **43. XSS in React/Angular**

Frameworks auto-escape; vulnerabilities arise with `dangerouslySetInnerHTML`/`[innerHTML]`. Sanitize and avoid interpolating raw HTML.

### **44. CSRF in SPAs**

Token-based APIs (Bearer) typically not CSRF-able unless cookies are **automatically** sent; if cookies used, require **SameSite=Lax/Strict**, CSRF tokens, and double-submit.

### **45. JWT storage best practice**

Prefer **httpOnly, secure, sameSite** cookies if server-side; if storing in memory, protect against XSS and refresh frequently.

---

### **46. Web Vitals: LCP, CLS, INP**

Optimize **LCP** (largest content paint) via critical CSS and early images; **CLS** via reserved space; **INP** via avoiding long tasks.

### **47. Resource hints**

`preload`, `prefetch`, `preconnect`, `dns-prefetch` to improve perceived performance and reduce TTFB for critical origins.

### **48. HTTP/2 vs HTTP/3 for SPAs**

H2 multiplexing reduces head-of-line blocking; H3/QUIC improves loss recovery on mobile. Tune server/ CDN to enable.

### **49. Image optimization**

Use **responsive `<img srcset/sizes>`**, AVIF/WebP, lazy-loading, and **intrinsic size** to avoid CLS.

### **50. Font loading**

Use `font-display: swap`/`optional`, subset fonts, and preconnect to font origins to minimize FOIT/FOUT.

---

### **51. Tree-shaking and side effects**

Ensure packages mark `"sideEffects": false` (or per-file list) and use **ESM**; avoid top-level mutations.

### **52. Dead code elimination pitfalls**

Dynamic `require`, mixing CJS/ESM, and `eval` impede shaking; prefer static imports.

### **53. Source maps in prod**

Host **separate, access-controlled** maps to aid debugging without leaking to public; scrub secrets from code.

### **54. Monorepos for micro-frontends**

Use **Nx/Turborepo** for caching and consistent tooling; enforce version constraints and single source of truth for design system.

### **55. Design systems & theming**

Encapsulate components, tokens, and accessibility rules; export **CSS variables** for runtime theming and **dark mode**.

---

### **56. CSS architectures (BEM, ITCSS) vs CSS-in-JS**

BEM/ITCSS scale with pure CSS; CSS-in-JS co-locates styles and supports theming/dynamic styles but adds runtime cost unless compiled (e.g., Linaria/vanilla-extract).

### **57. Tailwind vs CSS Modules**

Tailwind accelerates dev with utility classes and **design tokens**; CSS Modules keep semantic class names and isolate leakage; both can coexist.

### **58. Container queries & `:has()`**

**Container queries** adapt components to their container size; `:has()` enables parent-dependent styling — powerful for componentized layouts.

### **59. Grid subgrid**

`subgrid` lets children align with parent grid lines; simplifies complex layouts without manual column math.

### **60. Animations and performance**

Prefer **transform/opacity**; avoid layout-thrashing properties; use `will-change` sparingly and respect reduced-motion.

---

### **61. Angular template performance tips**

Use **OnPush**, `trackBy` in `*ngFor`, and pure pipes; avoid **heavy logic** in templates—push it to component/computed signals.

### **62. Angular routing optimization**

Lazy-load feature routes, **standalone route components**, and preloading strategies for frequent paths.

### **63. Angular Reactive Forms vs Template-driven**

Reactive forms offer **immutable updates**, granular validation, better testability; template-driven suits small/simple forms.

### **64. ControlValueAccessor**

Build **custom form controls** integrating with Angular forms API for consistent validation/touch/dirty states.

### **65. Angular SSR (Angular Universal)**

Pre-render for SEO and perf; hydrate client-side; ensure services are **platform-agnostic** (no direct `window`/`document`).

---

### **66. React forms at scale**

Use **react-hook-form** for uncontrolled inputs + refs; integrates with Zod/Yup; minimal rerenders vs Formik for large forms.

### **67. Form validation libraries**

Zod/Yup for schema validation; prefer **schema-driven** validation for consistency server ↔ client.

### **68. Data fetching patterns (React)**

SWR/React Query for cache + revalidation; Suspense-first APIs for RSC; use **`useEffect` sparingly** for fetching.

### **69. Handling API errors**

Normalize error shape, map to UX states, show **retry affordances**, and instrument with logs and **user fingerprint**.

### **70. Optimistic updates & rollbacks**

Apply UI updates before server confirms; rollback on failure; React Query provides `onMutate/onError/onSettled` hooks.

---

### **71. GraphQL vs REST in frontends**

GraphQL avoids **over/under-fetching**, supports **fragments** and **subscriptions**; REST remains simpler and cache-friendly with proper design.

### **72. GraphQL clients (Apollo/urql/Relay)**

Apollo: batteries-included; Relay: **edge-optimized, strict fragments**; urql: lightweight and modular.

### **73. WebSockets vs SSE vs Long polling**

WebSockets: **bi-directional**; SSE: **server→client** push over HTTP; long polling: fallback. Choose by infra constraints and bidirectional needs.

### **74. Uploading large files**

Chunked uploads, **tus** protocol, resumable with checksums; show progress and handle pause/resume.

### **75. PWA essentials**

Service Worker for **offline caching**, Web App Manifest, **background sync**, and push notifications with user consent.

---

### **76. Security: OAuth/OIDC in SPAs**

Use **Authorization Code + PKCE**; store tokens in cookies (httpOnly) or memory; never hardcode secrets in the client.

### **77. Prevent clickjacking**

Set `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'` on pages not meant to be embedded.

### **78. Input sanitization and DOM sinks**

Sanitize HTML, avoid innerHTML; centralize sanitizer utilities and security review gates in CI.

### **79. Handling secrets and envs in frontends**

Anything in the bundle is public; use **build-time env** only for non-secret flags; proxy secure calls through the server.

### **80. Dependency risk management**

Pin versions, enable `npm audit`, SCA scanners (Dependabot/Snyk), and **subresource locking** with `pnpm`/`npm lockfiles`.

---

### **81. Testing pyramid for frontends**

Unit (fast, many), component tests (RTL), **contract tests** for APIs, and selective E2E (Cypress/Playwright) for critical journeys.

### **82. React Testing Library principles**

Test like a user: query by role/label/text; avoid implementation details such as class names and internal state.

### **83. Mocking fetch/HTTP**

Use **MSW (Mock Service Worker)** to simulate network at the **service worker layer**—realistic and framework-agnostic.

### **84. Visual regression testing**

Percy/Chromatic/Applitools to catch CSS drift; integrate into PR checks with **thresholds**.

### **85. Linting & type safety**

ESLint with accessibility plugins, TypeScript strict mode, and **tsec**/**typescript-eslint** rules to prevent unsafe any/implicit any.

---

### **86. TypeScript advanced types for props**

Use **Discriminated Unions** for variant components, **Template Literal Types** for class utilities, and **satisfies** for config validation.

### **87. Generics in component libraries**

Generic props for `as` polymorphism (e.g., button as link) and data-grid models; ensure **inference friendly** API shapes.

### **88. Declaration merging & ambient types**

Augment third-party module types in `global.d.ts` to extend design system tokens, module interfaces, or env globals.

### **89. Build-time checks with Zod + TS**

Validate config and process env at runtime with Zod while using `z.infer<>` for static typing—closes the **type/behavior gap**.

### **90. DX enhancements**

Storybook for component docs, **CSF3** stories, auto-props tables, and **interaction tests**; colocation of stories with components.

---

### **91. Observability in SPAs**

Collect **Web Vitals**, error telemetry (window.onerror, unhandledrejection), trace IDs in headers, and correlate with backend APM.

### **92. Feature flags & experiment frameworks**

Use **server-driven** flags to gate features, run A/B tests, and ensure flags are **kill-switch ready**; clean up stale flags.

### **93. SEO for SPAs**

Use **SSR/SSG** or prerender, semantic HTML, structured data (JSON-LD), stable URLs, and `rel="canonical"`.

### **94. Analytics hygiene**

Defer non-essential analytics, respect **Do Not Track/consent**, and avoid blocking main thread with heavy trackers.

### **95. Error recovery UX**

Graceful fallbacks, retry buttons, **preserve user inputs**, and surface support codes with timestamps.

---

### **96. Offline-first conflict resolution**

Use client-side queues with **CRDTs** or **last-write-wins** strategies; show conflict UIs for manual merges where needed.

### **97. Large list CRUD patterns**

Cursor-based pagination, background prefetch of next pages, columnar virtualization, and **sticky filters**.

### **98. Printing and export**

Provide **print stylesheets**, CSV/Excel exports via **Web Workers**; stream large CSVs to avoid memory spikes.

### **99. Edge rendering**

Leverage edge functions/CDN for **personalized SSR close to users**; ensure deterministic hydration and cookie partitioning.

### **100. Production readiness checklist (frontend)**

Web Vitals budgets, preloading critical assets, error/retry strategy, auth timeout flows, **i18n coverage**, security headers (CSP/SRI), accessibility passes, and **CI gates** (lint, typecheck, tests, bundle size).

---

✅ **Section 3 complete: 100 Advanced Frontend Q&A.**
Ready to continue with **Section 4 — REST API & Hibernate/JPA (100 Advanced Q&A)** next?

Great — here’s **Section 4: REST API Design & Hibernate/JPA — 100 Advanced Questions + Answers**.
Concise, senior-level, and production-oriented.

---

## REST API (Design, HTTP, Security, Observability, Resilience)

1. **What makes an API “RESTful”?**
   Resource orientation, uniform interface (HTTP verbs), statelessness, cacheability, layered system, hypermedia controls where useful.

2. **Idempotency per HTTP verb?**
   GET/HEAD/OPTIONS/TRACE: safe & idempotent; PUT/DELETE: idempotent (not safe); POST/PATCH: not idempotent by default.

3. **Designing idempotent POST (payments/orders)?**
   Support `Idempotency-Key` header persisted server-side mapping request→result to dedupe retries.

4. **When to use PUT vs PATCH?**
   PUT replaces entire resource (client must send full representation); PATCH partially updates (JSON Patch/Merge Patch).

5. **Resource vs subresource URIs?**
   Top-level nouns (`/orders`), with subresources for containment (`/orders/{id}/items`). Avoid verbs in paths.

6. **When to nest vs link?**
   Nest for strong ownership/lifecycle coupling; link for related-but-independent aggregates (return HATEOAS links or IDs).

7. **Versioning strategies**
   URI (`/v1`), header (`Accept: application/vnd.company.v1+json`), or resource evolution via additive, backward-compatible changes. Prefer additive + deprecation policy.

8. **Content negotiation**
   Use `Accept` and `Content-Type`. Support multiple representations (JSON default; optionally CSV/NDJSON for exports/streams).

9. **Pagination best practices**
   Cursor-based for large/unstable datasets; include `next/prev` links & `X-Total-Count` (if cheap). Validate `size` limits to avoid abuse.

10. **Sorting & filtering**
    `?sort=field,asc&filter[status]=ACTIVE&filter[date][gte]=2025-01-01`. Document operators and validate field names.

11. **ETag/If-Match for concurrency**
    Return `ETag` on reads; require `If-Match` for updates to enforce optimistic concurrency at HTTP level.

12. **Caching headers**
    Use `Cache-Control`, `ETag`, `Last-Modified`, `Vary`. Public vs private caches; respect `must-revalidate` for correctness.

13. **HTTP status codes you should actually use**
    200/201/202/204; 304; 400/401/403/404/409/412/415/422; 429; 500/502/503/504. Be consistent.

14. **Problem Details (RFC 7807)**
    Standard error body: `type`, `title`, `status`, `detail`, `instance`, optional `errors[]`. Improves client handling.

15. **Bulk operations**
    Batch endpoints (`POST /orders:batchCreate`), atomic vs per-item results (207 Multi-Status). Consider job resources for long-running work.

16. **Async operations**
    Return 202 with `Location` to a job resource; clients poll job or subscribe to webhooks/events.

17. **Events & webhooks**
    Emit domain events (Outbox/CDC) and allow clients to register webhooks with retries + HMAC signatures for trust.

18. **Rate limiting**
    Use token bucket/leaky bucket; expose headers (`X-RateLimit-Limit/Remaining/Reset`). Consider per-API key, IP, tenant.

19. **API keys vs OAuth2/OIDC**
    API keys = simple identification; OAuth2 = delegated auth; OIDC adds identity. Prefer OAuth2/OIDC for user-facing flows.

20. **Scopes & fine-grained authorization**
    Design scopes per domain action (`orders:read`, `orders:write`). Support ABAC/RBAC in gateway or resource server.

21. **JWT pitfalls**
    Validate signature/alg, `exp`, `aud`, `iss`, clock skew. Never store secrets in JWT; rotate keys (JWKS). Keep TTL short.

22. **CSRF in cookie-based auth**
    Use `SameSite=Lax/Strict`, CSRF tokens, and double-submit. With bearer tokens (not automatically sent), CSRF risk drops.

23. **Input validation & error semantics**
    Validate at boundary; return 422 with field-level errors; reject unknown fields if strict mode.

24. **Output shaping**
    Sparse fieldsets `?fields=…` and embedding `?include=…` to control payload size (document defaults & limits).

25. **N+1 over the wire**
    Bundle dependent reads via composite endpoints or GraphQL; or introduce `/search`/`/report` endpoints.

26. **Security headers**
    CSP, X-Content-Type-Options, Referrer-Policy, X-Frame-Options/`frame-ancestors`, HSTS for TLS.

27. **API gateway responsibilities**
    AuthN/Z offload, rate limit, routing, canary, WAF, schema enforcement, central observability. Keep business logic in services.

28. **Schema-first vs code-first**
    Schema-first (OpenAPI) gives stronger governance; code-first iterates faster. Many teams generate both ways, but enforce linting.

29. **OpenAPI docs quality**
    Examples, enums with descriptions, error models, pagination schemas, security schemes, and `links` for follow-ups.

30. **Contract testing**
    Use Pact/contract tests to ensure provider meets consumer expectations; prevents breaking changes across teams.

31. **Observability**
    Correlate requests with `traceId/spanId`. Emit structured logs, metrics (latency, error rate), distributed traces across services.

32. **SLOs for APIs**
    Define targets for availability, latency percentiles, and error budgets; drive capacity and release policies.

33. **Timeouts & retries**
    Client timeouts must be stricter than server; idempotent operations only; backoff + jitter; avoid retry storms.

34. **Circuit breaking**
    Trip on high error rate/latency; return fast failures and optionally fallback. Protects downstream and callers.

35. **Bulkhead isolation**
    Separate pools/queues per dependency/tenant to prevent cascading saturation.

36. **Request size & upload patterns**
    Limit `Content-Length`; use multipart, presigned URLs to object storage; process uploads async.

37. **Internationalization**
    Honor `Accept-Language`; keep server messages stable or use error codes + client-side localization.

38. **Dealing with large exports**
    NDJSON/CSV streaming with `Transfer-Encoding: chunked`. Avoid loading entire result sets in memory.

39. **Soft deletes vs hard deletes**
    Soft delete for audit/recovery; expose filter `?includeDeleted=`; ensure unique constraints consider the soft-delete flag.

40. **Tenancy models**
    Header (`X-Tenant`), subdomain, or DB/schema per tenant. Enforce tenant filters in every DB access path.

---

## Hibernate / JPA (Mapping, Queries, Transactions, Performance)

41. **Entity vs DTO**
    Entities reflect persistence model and lifecycle; DTOs shape API contracts. Don’t expose entities directly to controllers.

42. **Owning side of relationships**
    The side with the foreign key (mappedBy **absent**) is owning; only owning side updates join column. In many-to-many, the join table owner.

43. **Fetch types**
    `LAZY` recommended for collections & @ManyToOne; avoid `EAGER` (surprising SQL, N+1, huge graphs).

44. **N+1 query problem**
    Accessing lazy collections across a list causes extra queries. Fix with fetch joins, batch fetching, or entity graphs.

45. **Fetch join caveats**
    One collection fetch join per query limit (cartesian explosion). Use pagination carefully (DB applies after join).

46. **`@EntityGraph`**
    Declaratively define fetch plans per use case; safer than blanket `EAGER`.

47. **DTO projections**
    Use constructor projections or Spring Data interface projections for thin, fast reads (skip entity hydration).

48. **Criteria API vs JPQL**
    Criteria = type-safe, dynamic; JPQL = concise for static queries. Use Specification pattern for composable filters.

49. **Flush modes**
    `AUTO` (default) flushes before query that depends on changes; `COMMIT` defers. Set carefully to avoid stale reads.

50. **Persistence context (first-level cache)**
    Ensures identity per transaction; repeated finds return same instance; dirty checking at flush time.

51. **Second-level cache**
    Shared across sessions (Ehcache, Caffeine, Infinispan). Cache immutable aggregates and reference data; avoid caching volatile entities.

52. **Query cache**
    Caches result sets; must be used with L2 cache for entities; sensitive to parameters & invalidation. Use sparingly.

53. **Batch fetch size**
    `@BatchSize(size=50)` or global setting fetches lazy collections in groups to reduce round-trips.

54. **`hibernate.jdbc.batch_size`**
    Enables statement batching for inserts/updates. Combine with ordered inserts/updates to maximize batchability.

55. **Cascade types**
    `PERSIST`, `MERGE`, `REMOVE`, `REFRESH`, `DETACH`, `ALL`. Use narrowly; don’t cascade REMOVE from parent when children are shared.

56. **`orphanRemoval = true`**
    Removes child rows when they’re removed from the collection — great for aggregates; beware accidental deletes.

57. **Optimistic locking with `@Version`**
    Detect concurrent updates; raise `OptimisticLockException`. Bubble to API as 409 Conflict (or 412 if using ETag).

58. **Pessimistic locks**
    `PESSIMISTIC_READ/WRITE` with `@Lock`/`LockModeType`. Prevent conflicts on hot rows; watch for deadlocks.

59. **Equals/hashCode for entities**
    Use business key or synthetic id cautiously. Avoid including lazy collections; be proxy-safe.

60. **`@ManyToMany` antipattern**
    Often replace with two `@OneToMany` via explicit join entity to attach attributes and control lifecycle.

61. **Embeddables**
    `@Embeddable` value types for reuse (address, money). Stored in same table; no identity.

62. **Inheritance strategies**
    `SINGLE_TABLE` (fast, nullable columns), `JOINED` (normalized, joins), `TABLE_PER_CLASS` (rare). Choose per query needs.

63. **Attribute converters**
    `@Converter` for custom mappings (e.g., encrypt strings, map JSONB to objects). Keep deterministic, fast.

64. **Database enums**
    Prefer string persisted values for evolvability; if native enums used, handle migration carefully.

65. **JSON/JSONB columns**
    Map via converter or Hibernate Types; index with GIN (PostgreSQL). Great for schemaless attributes.

66. **Auditing**
    Use Hibernate Envers or manual `createdAt/By`, `updatedAt/By`. For full history, Envers or event sourcing.

67. **Soft delete with filters**
    `@SQLDelete` + `@Where` to filter out deleted rows automatically. Remember admin/reporting paths need overrides.

68. **Read consistency & isolation**
    Set DB isolation (often READ COMMITTED). For replicas, ensure read-your-writes or stickiness after writes.

69. **Transaction boundaries**
    Service layer demarcation (`@Transactional`). Keep transactions short; no network calls inside if possible.

70. **`@Transactional` propagation**
    `REQUIRED` default; `REQUIRES_NEW` for outbox/audit side effects; `NESTED` with savepoints (DB support needed).

71. **Handling large write loads**
    Use batch inserts, disabled flush every N records, turn off second-level cache during bulk jobs.

72. **Bulk JPQL updates/deletes**
    Operate directly in DB, bypass persistence context; clear/evict PC to avoid stale entities.

73. **Lazy initialization exceptions**
    Accessing lazies outside transaction/session. Fix with fetch plan, DTO projection, or Open Session in View (discouraged).

74. **Open Session in View (OSIV)**
    Keeps session open across web tier; simplifies lazies but risks N+1 & transaction semantics confusion. Prefer DTO shaping.

75. **Transaction-outbox integration**
    Save event in same txn as entity; a relayer publishes to Kafka. Guarantees atomicity and eventual delivery.

76. **CQRS with JPA**
    Commands mutate aggregates (JPA); queries hit read-optimized schemas or projections. Separate models for scale.

77. **Hibernate Reactive**
    Asynchronous, non-blocking API (Mutiny/Stage). Use when IO-bound & reactive stack (WebFlux/Vert.x). Different Session API.

78. **Multitenancy**
    DATABASE/SCHEMA/TABLE discriminator. Use `CurrentTenantIdentifierResolver` or filters; ensure every query enforces tenant.

79. **Connection pool (HikariCP) tuning**
    Pool size ≤ DB max; monitor wait time; set timeouts; test on borrow; enable leak detection.

80. **Query plan analysis**
    Use `EXPLAIN` to verify indexes and join orders; fix with composite indexes matching predicate order & selectivity.

81. **Pagination with large offsets**
    Use keyset pagination (`WHERE (date,id) < (?,?) ORDER BY date DESC, id DESC LIMIT ?`) to avoid deep offset scans.

82. **Handling uniqueness at scale**
    DB unique constraints as final guard; implement “reserve-then-confirm” semantics or upserts for race conditions.

83. **Upsert patterns**
    Use DB-specific `INSERT … ON CONFLICT DO …` (Postgres) or merge semantics; with JPA, call native queries or event-based reconciliation.

84. **Time zones**
    Store UTC in DB, convert at edges. Use `OffsetDateTime`/`Instant`. Ensure JDBC driver config and Hibernate type mapping.

85. **Binary large payloads**
    Store in object storage; keep DB URI/metadata. Streaming endpoints + presigned URLs.

86. **Validation layers**
    Bean Validation for request→DTO; domain invariants in entities; DB constraints for final enforcement. All three complement.

87. **Migrations**
    Flyway/Liquibase run pre-boot in CI/CD or app startup. Zero-downtime: backward-compatible migrations first, code second, cleanup later.

88. **Index hygiene**
    Avoid redundant indexes; monitor bloat; add partial/conditional indexes for sparse columns.

89. **Deadlock handling**
    Detect and retry short idempotent transactions; reduce lock scope and consistent ordering of updates.

90. **Read replicas**
    Route GETs to replicas when staleness acceptable; maintain session stickiness post-write for read-your-writes flows.

91. **`@MapsId`**
    Share primary key with parent (one-to-one strong ownership). Good for extension tables.

92. **`@NaturalId`**
    Second identifier besides PK (e.g., `email`). Cacheable; simplifies lookups and constraints.

93. **`@Subselect` (Hibernate)**
    Map read-only entity to a SQL subselect/view for reporting; not updatable.

94. **`@Formula`**
    Computed columns via SQL expressions — use sparingly; watch portability & performance.

95. **`@WhereJoinTable` (Hibernate)**
    Filter many-to-many join rows (soft delete / flags). Vendor-specific.

96. **Savepoint/Nested transactions**
    `PROPAGATION_NESTED` uses DB savepoints; useful for partial rollbacks in batch steps.

97. **Lock timeouts & hints**
    Set lock timeout to avoid indefinite waits; vendor hints (e.g., `FOR UPDATE SKIP LOCKED`) for queue workers.

98. **Jackson & JPA pitfalls**
    Infinite recursion on bi-directional relations. Use DTOs or Jackson annotations (`@JsonIgnore`, `@JsonIdentityInfo`) carefully.

99. **`Serializable` in entities**
    Not required; avoid Java serialization. Prefer JSON for messages; disable serialization on entities to prevent accidental use.

100. **Production checklist (JPA)**
     Right fetch plans; DTO projections for reads; batching and connection pool tuned; 2LC only for reference data; optimistic locking with clear 409 semantics; schema migrations; tenant enforcement; observability (slow query logs); and well-documented SLOs.

---

✅ **Section 4 complete: 100 Advanced REST + Hibernate/JPA Q&A.**
Shall I proceed with **Section 5 — DevOps: Docker, Terraform, GitHub, Jenkins (100 Advanced Q&A)** next?

Perfect ✅

Here’s **Section 5 – DevOps: Docker | Terraform | GitHub | Jenkins (100 Advanced Q&A)** — focused on how a senior backend/full-stack engineer explains real-world CI/CD, infra-as-code, and containerization decisions.

---

## **Docker – Images | Containers | Networking**

**1.** Difference between images & containers?
An *image* is a read-only snapshot (template); a *container* is its runtime instance with a writable layer.

**2.** Layers & union FS?
Each Dockerfile instruction adds an immutable layer; the top writable layer records changes. Reuse of cached layers speeds builds.

**3.** What happens under `docker build .`?
Docker daemon parses `Dockerfile`, builds layers from base→top, tags image, stores in local registry (`/var/lib/docker`).

**4.** Best-practice Dockerfile structure?
Base → deps → copy → build → expose → CMD.
Use multi-stage builds, `.dockerignore`, non-root user, health check, minimal base (`distroless`, `alpine`).

**5.** Difference between `CMD` and `ENTRYPOINT`?
`ENTRYPOINT` defines executable; `CMD` supplies defaults. Combine for overridable arguments.

**6.** Why multi-stage builds?
Separate build & runtime layers → smaller, secure images; drop compilers/SDKs after copy of artifacts.

**7.** How to reduce image size?
Use `--no-cache` judiciously, multi-stage, clean temp files, merge RUNs, base on `scratch/alpine`, leverage `.dockerignore`.

**8.** Container networking modes?
bridge (default NAT), host (shared stack), none, overlay (swarmed).
Bridge = isolation; host = perf; overlay = multi-host.

**9.** Container DNS resolution?
Docker’s embedded DNS assigns names equal to service/container name inside networks.

**10.** Volume vs bind mount?
Volume managed by Docker – persistent, portable.
Bind mount links host path – useful for dev.

**11.** How to inspect resource limits?
`docker stats`, `docker inspect`. Apply cgroup limits via `--memory`, `--cpus`.

**12.** Copy-on-write penalties?
Frequent writes to layered FS degrade I/O. Mitigate via volumes for hot data.

**13.** Docker Compose orchestration basics?
Declarative YAML to build/run multi-container stacks (`depends_on`, `networks`, `volumes`, `env_file`). Ideal for local dev.

**14.** Health checks & restart policies?
`HEALTHCHECK CMD`; policies: `always`, `on-failure`, `unless-stopped`. Enables self-healing.

**15.** Security best practices**
Run as non-root, pin base digests, sign images (Cosign/Notary), scan via Trivy/Grype, limit capabilities, readonly FS.

**16.** Container runtime vs engine**
Engine = Docker daemon; runtime = runc/containerd responsible for low-level isolation.

**17.** Ephemeral vs persistent data**
Stateless apps store data externally (DB, object store). Volumes only for cache/temp.

**18.** How to share env vars securely?**
Use `.env` for local; secrets manager or encrypted CI vars for prod. Avoid committing secrets.

**19.** Multi-arch images**
Manifest lists per arch (amd64/arm64). Built via `docker buildx`.

**20.** OCI compliance**
Open Container Initiative defines image & runtime specs ensuring portability (Docker, Podman, containerd).

---

## **Terraform – Infrastructure as Code**

**21.** Core workflow?
Write → `terraform init` → `plan` → `apply` → `destroy`.
State captures current infra; plan diff previews changes.

**22.** State file purpose?
Tracks resource IDs & metadata for drift detection. Sensitive; store remotely (S3 + DynamoDB lock).

**23.** How does remote state locking work?**
Backend plugin (e.g., S3/DynamoDB) creates a lock record preventing concurrent applies.

**24.** Providers & resources?**
Provider = API client; resource = declarative object. Each resource maps to an API call lifecycle.

**25.** Modules**
Reusable templates with `variables`, `outputs`. Versioned via registry/Git; compose infra hierarchically.

**26.** Variables & locals**
Variables: inputs; locals: computed values; prefer locals for derived expressions.

**27.** Outputs usage**
Expose IDs, URLs for cross-module references or CI outputs.

**28.** Terraform Cloud vs local CLI**
Cloud provides remote runs, policy as code (Sentinel), drift detection, secure state.

**29.** Workspaces**
Lightweight state separation (dev/stage/prod). Alternative to directory per-env pattern.

**30.** `depends_on` necessity**
Used when implicit dependency (reference) missing; ensures deterministic creation order.

**31.** Terraform graph & parallelism**
DAG-based execution; defaults to 10 parallel resources; tweak via `-parallelism`.

**32.** Lifecycle meta-args**
`create_before_destroy`, `prevent_destroy`, `ignore_changes` for zero-downtime & drift-tolerance.

**33.** `terraform import` use case**
Bring existing resources under management; verify plan afterwards.

**34.** `for_each` vs `count`**
`for_each` maps by key → stable addresses; `count` uses index → reorder issues.

**35.** Sensitive vars**
`variable "s3_key" { sensitive = true }` masks output; still encrypt state externally.

**36.** Remote backends examples**
S3/DynamoDB, GCS, Azure Blob, Terraform Cloud, Consul.

**37.** Data sources**
Read-only lookups (e.g., existing AMI, VPC id) used in interpolation.

**38.** Plan file security**
`terraform plan -out=plan.tfplan` may contain secrets → handle as sensitive artifact.

**39.** Managing provider versions**
Pin versions in `required_providers`; prevents breaking upgrades.

**40.** How to enforce compliance?**
Sentinel/OPA/Conftest for policy-as-code; validate naming, tags, encryption.

**41.** Zero-downtime deploys (blue/green)**
Create new infra (`create_before_destroy`), switch traffic via LB, then destroy old.

**42.** State drift detection**
`terraform plan -refresh-only` to reconcile with live infra.

**43.** Terraform vs Pulumi vs CDK**
Terraform → HCL; Pulumi/CDK → general-purpose languages. Terraform wins on ecosystem maturity.

**44.** Multi-provider modules**
Parametrize providers (e.g., AWS+Azure). Use alias providers within same config.

**45.** Terragrunt**
Wrapper adding DRY hierarchy, remote state, and dependency orchestration between modules.

**46.** Templating with `templatefile()`**
Injects dynamic configs (e.g., user-data scripts) from external files.

**47.** Cross-region replication pattern**
Define provider alias per region; replicate resources & replicate state outputs.

**48.** Drift-free secrets**
Use external vaults & data sources rather than inline secrets; rotate via pipeline, not apply.

**49.** Testing Terraform**
Use `terraform validate`, `tfsec`, `checkov`, and Terratest (Golang) for automated tests.

**50.** Team workflow**
Git PR → CI runs `plan` → manual/auto apply → tag release → audit logs via remote backend.

---

## **GitHub – Source Control | Actions | Security**

**51.** Branching models**
Git Flow (main/develop), GitHub Flow (single main + PRs), Trunk-based (short-lived branches).

**52.** Pull request quality gates**
Require reviews, status checks (tests/lint/build), and signed commits.

**53.** Git hooks & automation**
Pre-commit lint, secret scans; enforce via Husky or GitHub Actions.

**54.** GitHub Actions workflow syntax**
YAML triggers (`on:`), jobs, steps; runs on hosted runners or self-hosted.

**55.** Matrix builds**
Run jobs across multiple OS/Java versions via `strategy.matrix`.

**56.** Caching dependencies**
Use `actions/cache` keyed by lock files to speed builds.

**57.** Reusable workflows**
`workflow_call` for central CI templates; promote consistency across repos.

**58.** Secrets management**
Store encrypted secrets in repo/org; mask in logs; rotate via API; prefer environment secrets per env.

**59.** Environments & approvals**
`environment:` defines prod/stage; can require reviewers before deploys.

**60.** Artifacts & build outputs**
`actions/upload-artifact` for build packages; download in later jobs.

**61.** Conditional jobs**
Use `if:` expressions (`github.ref == 'refs/heads/main'`).

**62.** Self-hosted runners security**
Isolate per team/env; update regularly; restrict job scopes; never run untrusted forks.

**63.** Dependabot / security scanning**
Automated PRs for vuln deps; integrate code QL & secret scanning.

**64.** GitHub Packages registry**
Private Maven/NPM/Docker registry; authenticate via PAT or GITHUB_TOKEN.

**65.** Git tags & releases**
Semantic version tags drive release notes and deployments; automate changelogs via conventional commits.

**66.** Protected branches**
Block force-push; enforce PR checks; signed commits; limit who can merge.

**67.** Monorepo scaling**
Use Nx/Turborepo caching; split workflows per path filter to run partial CI.

**68.** Issue/PR templates**
Standardize bug/feature reporting; auto-assign labels via `YAML` metadata.

**69.** Actions vs Workflows**
Action = reusable step; Workflow = orchestrates actions. Publish custom actions in Marketplace.

**70.** Auditing & compliance**
Use org audit log, branch protection, signed tags; export to SIEM.

---

## **Jenkins – Pipelines | CI/CD | Integrations**

**71.** Declarative vs Scripted pipelines**
Declarative (YAML-like `pipeline {}`) simpler; scripted (Groovy) full control. Prefer declarative for consistency.

**72.** Pipeline stages example**
`checkout → build → test → package → docker build/push → deploy`.

**73.** Shared Libraries**
Centralized Groovy functions; versioned; loaded via `@Library`. Promote DRY pipelines.

**74.** Credentials management**
Store in Jenkins Vault; access via `withCredentials`; mask in logs.

**75.** Agents**
Master-agent architecture; ephemeral agents via Docker or Kubernetes plugin for scalability.

**76.** Blue Ocean**
Modern UI plugin visualizing stages and parallel branches.

**77.** Parallel stages**
`parallel { stage('unit') {…} stage('integration') {…} }` – speeds builds.

**78.** Post actions**
`post { success { … } failure { … } always { … } }` for notifications & cleanup.

**79.** Parameterized builds**
Input parameters for manual triggers (branch, tag, version).

**80.** Multibranch pipelines**
Auto-discover `Jenkinsfile` per branch; integrates with GitHub webhooks.

**81.** Webhooks vs polling**
Webhooks push events (efficient); polling wastes cycles. Prefer webhook triggers.

**82.** Artifact retention & archiving**
`archiveArtifacts` to keep build outputs; set retention policies to manage disk.

**83.** Integrating Docker**
Use `agent { docker { image 'maven:3.9-jdk21' } }`; isolates builds and dependencies.

**84.** Kubernetes plugin**
Spawns ephemeral pods per build; declarative pod templates for tool images.

**85.** Pipeline as Code**
Store `Jenkinsfile` in repo; PR-tested automatically; versioned history.

**86.** Retry & timeout handling**
`retry(3) { … }`, `timeout(time:10,unit:'MINUTES') { … }` for resilient stages.

**87.** Notifications**
Slack/email/webhook via plugins; send on `failure`/`unstable`.

**88.** Build promotion & environments**
Separate jobs for dev/test/prod; promote artifact tags through environments with approvals.

**89.** Security hardening**
Role-based auth, CSRF protection, restrict script execution sandbox, TLS, backup secrets.

**90.** Jenkins vs GitHub Actions vs GitLab CI**
Jenkins = most flexible/self-hosted; GH Actions = tight GitHub integration; GitLab CI = built-in RBAC/artifacts; choose by ecosystem & governance.

---

## **CI/CD Cross-Cutting**

**91.** Pipeline triggers**
On commit, tag, PR, cron, manual, or API. Combine for scheduled releases & nightly tests.

**92.** Blue/Green vs Canary**
Blue/Green = two stacks, instant switch; Canary = gradual traffic shift + metrics rollback.

**93.** Artifact promotion**
Immutable build artifact moves across envs; no rebuilds between stages (ensures reproducibility).

**94.** Rollback strategy**
Versioned artifacts + infra; use feature flags, DB migrations backward-compatible; maintain N-1 readiness.

**95.** Secrets management across pipelines**
Centralize in Vault/Azure Key Vault/Secrets Manager; inject via short-lived tokens; avoid plaintext.

**96.** Observability in CI/CD**
Emit build duration, queue time, test pass %, failure causes; push to Prometheus/Grafana for SLA monitoring.

**97.** Compliance checks**
Lint Dockerfiles, scan dependencies, verify signatures, enforce license policy via CI stage.

**98.** Immutable infra principle**
Never patch servers manually; rebuild images via pipeline on each change.

**99.** Self-service pipelines**
Templates & GitOps triggers let teams onboard new services without ops tickets.

**100.** End-to-end deployment flow (summary)**
Push → CI build → unit/integration tests → image scan → Terraform plan → approval → apply → deploy to K8s → post-deploy tests → notify → observe → rollback if SLO breach.

---

✅ **Section 5 complete — 100 Advanced DevOps Q&A**

Next section:
**Section 6 – Testing (TDD, BDD, JUnit5, Mockito, Cucumber) – 100 Advanced Q&A**.
Would you like me to continue with that one?

You're right—picking up where we left off at **#99**. Here are the last two to complete **Section 6 – Testing (100 Advanced Q&A)**:

---

**99. What is Continuous Testing and how do you “shift left” and “shift right”?**
Continuous Testing runs the right tests at every pipeline stage to give **risk-based feedback** fast.

* **Shift left:** earlier unit/contract/perf smoke in PRs; ephemeral envs; contract tests block merges; mutation testing to harden unit tests.
* **Shift right:** canary verifications, synthetic probes, error budgets, real-user monitoring (RUM), chaos/latency injection in lower traffic; auto-rollback on SLO breach.
  Tie both ends with **feature flags** and **observability** so experiments are safe and reversible.

**100. Final testing checklist before production release**

* **Coverage quality:** statement/branch OK + **mutation score** meaningful.
* **Determinism:** no flakes; time/UUID/network mocked; fixed seeds.
* **Contracts:** consumer/provider verified; OpenAPI validated; examples tested.
* **Security:** ZAP/DAST pass; secrets not logged; dependencies scanned.
* **Data:** migrations reversible; seed data/version checks in CI.
* **Resilience:** timeouts, retries, circuit breakers covered by tests; failure drills pass.
* **Performance:** budgeted p95/p99 latency, throughput, and footprint captured per build.
* **Observability:** structured logs + trace IDs, metrics + alerts, golden signals dashboards.
* **Rollbacks:** artifact immutability, DB backward compatibility, runbooks ready.

---

✅ **Section 6 complete — 100 Advanced Testing Q&A.**

Want me to generate **Section 7 — Azure (App Service, AAD, Key Vault, Storage, ADO Pipelines, Monitoring) — 100 Advanced Q&A** next, in the same full Q&A format?

Perfect ✅

Here’s **Section 7 – Microsoft Azure Cloud (100 Advanced Q&A)** — tailored for senior backend/full-stack engineers working with Java / Spring Boot / CI / DevOps workloads on Azure.

---

## ☁️ Azure Architecture & Core Concepts

**1. What’s the Azure Resource Manager (ARM) model?**
ARM is Azure’s control-plane API. Every resource is created via an *ARM template* or REST call inside a *resource group*. It supports declarative IaC, RBAC, tags, locks, and consistent lifecycle management.

**2. Resource Group vs Subscription vs Tenant**

* **Tenant:** AAD directory boundary.
* **Subscription:** billing + RBAC boundary.
* **Resource Group:** logical grouping within a subscription for lifecycle/unit of deployment.

**3. Azure regions & availability zones**
Regions = geo-clusters; zones = physically separate data centres within region. Use zonal or zone-redundant deployments for 99.99 % availability.

**4. Paired regions — why important?**
Each region has a designated pair (e.g. UK South ↔ UK West) for disaster recovery, replication, and sequenced updates to avoid simultaneous outages.

**5. Azure Resource Locks**

* `ReadOnly` prevents changes.
* `CanNotDelete` protects critical infra (e.g., Key Vault). Useful for governance.

**6. What’s Azure Policy?**
Declarative rules enforcing governance (allowed locations, SKU, tag requirements). Evaluated by Policy engine at deployment and periodically for drift.

**7. How does RBAC work?**
Built on AAD principals (users/groups/service principals) granted roles at scopes (subscription → resource group → resource). Roles aggregate permissions (actions + dataActions).

**8. Managed Identities**
System Assigned (tied to resource) and User Assigned (reusable). Provide AAD token for Azure APIs without storing secrets.

**9. ARM Templates vs Bicep vs Terraform**
ARM = JSON, verbose; Bicep = DSL for ARM; Terraform = multi-cloud. All use ARM as backend. Bicep compiles to ARM natively.

**10. Azure Blueprints**
Bundle policy, RBAC, and templates for enterprise-wide governance (landing zones).

---

## ☸️ Compute & Containers

**11. App Service Plan vs App Service**
Plan = compute SKU (shared to dedicated VMs); App Service = deployed app instances running on that plan.

**12. How does scaling work for App Service?**
Manual or autoscale based on metrics (CPU, requests, queue length). Scale-out adds instances; scale-up changes SKU.

**13. Deployment Slots**
Staging environments on same plan; swap slots atomically for zero-downtime releases. Support warm-up hooks and swap with preview.

**14. Azure Functions consumption plan vs premium**
Consumption = serverless, billed per execution; cold starts. Premium = pre-warmed instances, VNet integration, long-running durable functions.

**15. Durable Functions**
Orchestrations built on Event Sourcing pattern for stateful serverless workflows (e.g., fan-out/in patterns).

**16. Container Apps vs AKS**
Container Apps = managed KEDA/Dapr platform for microservices without cluster ops. AKS = full Kubernetes control plane for complex orchestration.

**17. Azure Kubernetes Service (AKS) internals**
Managed control plane; nodes in user subscription. Integrates with Azure CNI, Managed Identity, and Azure Monitor for containers.

**18. Node pools and taints/tolerations**
Dedicated node sets per workload class (e.g., GPU pool). Taints = repel pods unless tolerated; supports cost/perf segmentation.

**19. Ingress on AKS**
NGINX Ingress Controller or Application Gateway Ingress Controller (AGIC) for L7 routing + TLS termination + WAF.

**20. Azure Container Registry (ACR)**
Private OCI registry with geo-replication, content trust, and webhooks. Integrates with AKS pull via Managed Identity.

---

## 🗃️ Storage & Data Services

**21. Azure Storage Account types**
Standard (LRS, ZRS, GRS) and Premium (BlockBlob/File). Contains Blob, File Share, Queue, Table services.

**22. Blob tiers**
Hot = frequent, Cool = infrequent (30 days), Archive = offline. Lifecycle rules automate tier transition.

**23. Static website hosting**
Enable on blob container (`$web`); serves via HTTPS with CDN integration.

**24. Azure Files vs Blob**
Files = SMB/NFS mount; Blob = object storage via HTTP. Use Files for legacy apps needing POSIX semantics.

**25. Azure SQL Database deployment models**
Single, Elastic Pool, Managed Instance. Elastic = shared DTUs; Managed Instance ≈ SQL Server full compatibility.

**26. Automatic tuning & Query Store**
Azure SQL analyzes plans and applies forced plan corrections; Query Store tracks regressions.

**27. Cosmos DB consistency levels**
Strong, Bounded Staleness, Session (default), Consistent Prefix, Eventual. Trade-off between latency and consistency.

**28. Cosmos DB partitioning**
Select partition key with high cardinality to distribute RUs; avoid hot partitions.

**29. Data Lake Gen 2**
Hierarchical namespace + POSIX ACLs on Blob storage for analytics (HDFS-compatible).

**30. Synapse Link**
Real-time integration from Cosmos DB to Synapse Analytics without ETL.

---

## 🔐 Security & Identity

**31. Azure AD vs AAD B2C**
AAD = workforce identity; B2C = customer identity with social providers and custom policies.

**32. OAuth2 flows supported by AAD**
Auth Code (+ PKCE), Client Credentials, Device Code, Implicit (legacy). Use v2.0 endpoints.

**33. Service Principals**
App identities in AAD for automation and CI/CD. Use Client Secret or Certificate credentials.

**34. Managed Identity vs Service Principal**
Managed Identities are rotated automatically and don’t require secret storage. Prefer them inside Azure.

**35. Key Vault secret vs key vs certificate**
Secret = value (string); Key = crypto material (RSA/ECC); Certificate = bundle of both + metadata.

**36. Access Key Vault from Spring Boot**
Use `spring-cloud-azure-starter-keyvault-secrets`; values load as PropertySources.

**37. Azure Disk Encryption**
Uses BitLocker or dm-crypt with Key Vault-stored keys and AAD integration.

**38. Network Security Groups (NSG)**
Stateless L3/4 firewall rules on subnets or NICs. Evaluate priorities (lowest wins).

**39. Private Link & Endpoints**
Private IP connectivity to PaaS services via Microsoft backbone — eliminates public exposure.

**40. Defender for Cloud**
Unified threat protection, secure-score tracking, and recommendations for VMs, K8s, and data resources.

---

## 🌐 Networking & Integration

**41. VNet vs Subnet**
VNet = private address space; Subnets = segments with NSGs and UDRs.

**42. VNet peering**
Connect VNets privately across regions; low latency; non-transitive by default.

**43. ExpressRoute vs VPN Gateway**
ExpressRoute = dedicated MPLS link with QoS; VPN = IPsec over Internet. Use ExpressRoute for regulated workloads.

**44. Application Gateway vs Load Balancer**
App GW = L7 reverse proxy (WAF, SSL offload); LB = L4 traffic distribution.

**45. Azure Front Door vs Traffic Manager**
Front Door = global edge CDN + Anycast load balancer. Traffic Manager = DNS-based failover.

**46. Service Bus vs Event Hub vs Event Grid**
Service Bus = enterprise queue/topic; Event Hub = high-throughput stream; Event Grid = reactive event routing.

**47. Dead-letter queues**
Store undeliverable messages for manual inspection and replay.

**48. Azure API Management (APIM)**
Full API gateway with rate-limiting, policies, transformations, developer portal, and OAuth2 integration.

**49. Logic Apps vs Functions**
Logic Apps = workflow designer; Functions = code. Combine for integration scenarios.

**50. Hybrid connections**
Secure relay to on-prem services without VPN via Service Bus Relay or Private Endpoint.

---

## ⚙️ DevOps & Pipelines

**51. Azure DevOps Pipelines vs GitHub Actions**
ADO = enterprise suite (board, repos, pipeline, artifact). GH Actions = lightweight YAML CI/CD tightly coupled to GitHub.

**52. Pipeline stages & approvals**
Define multi-stage YAML; add manual approvers on environments for prod promotion.

**53. Self-hosted agents**
Custom VMs or containers with custom toolchains; isolate secrets per team.

**54. Variable groups and key vault integration**
Link KV secrets to pipeline variables dynamically; rotation handled by Vault.

**55. Artifacts feed**
Package registry (Maven, NPM, NuGet). Immutable versions ensure reproducible builds.

**56. Service connections**
Secure endpoint definitions to deploy to Azure, K8s, DockerHub, etc.

**57. Deployment strategies**
Run tests → stage → prod via blue/green, canary, or ring based on metrics.

**58. Infrastructure pipelines**
Terraform/Bicep validated via ADO tasks with `plan` review before apply.

**59. Build templates**
YAML templates (`extends:`) for shared steps across repos.

**60. Pipeline caching**
Reuses Maven/NPM dependencies between runs to cut build times.

---

## 🧰 Monitoring & Observability

**61. Azure Monitor architecture**
Unified platform collecting metrics, logs, alerts, traces from resources. Backed by Log Analytics workspace.

**62. Application Insights**
Telemetry SDK for APM (traces, exceptions, dependencies). Integrates with Spring via OpenTelemetry bridge.

**63. Log Analytics Workspace and Kusto Query Language (KQL)**
Central store for logs; KQL supports joins, summaries, time charts. Use for dashboards and alert queries.

**64. Metrics vs Logs vs Traces**
Metrics = numeric time-series; Logs = events; Traces = distributed spans. Correlate via Operation ID.

**65. Custom metrics**
Push via Azure Monitor Metrics API or Micrometer bridge for Spring Boot Actuator.

**66. Alerts & Action Groups**
Alert rules trigger Action Groups (email, Logic App, Webhook, ITSM).

**67. Workbooks & Dashboards**
Interactive visual KQL reports for Ops/Dev. Shareable across teams.

**68. Application Map**
AI feature auto-discovers dependencies and latencies between services.

**69. Availability tests**
Synthetic ping tests from multiple regions to measure external uptime.

**70. Log retention & cost control**
Set data retention periods, table specific policies, and use archive/capacity reservations to cut costs.

---

## 🔄 Resilience & Disaster Recovery

**71. Azure Backup vs Site Recovery**
Backup = file/VM snapshots. ASR = replication and failover for entire VM/workload.

**72. Geo-redundant storage (GRS)**
Async replication to paired region for disaster recovery.

**73. Zone-redundant services**
App Service, SQL, Storage ZRS provide automatic cross-zone redundancy.

**74. Recovery Time Objective (RTO) vs Recovery Point Objective (RPO)**
RTO = max downtime; RPO = max data loss window. Drive DR strategy and replication frequency.

**75. Traffic failover**
Front Door / Traffic Manager redirect traffic to healthy region automatically.

**76. Chaos Studio**
Fault injection service for resilience testing (VM shutdown, latency injection).

**77. Health Probes integration**
Load balancers use HTTP/TCP health probes to remove unhealthy instances.

**78. Auto-healing App Service**
Custom rules restart process based on memory/response time thresholds.

**79. Scaling beyond region**
Multi-region deployment behind Front Door with geo-replicated data layer.

**80. Testing DR plans**
Run planned failovers regularly with readiness checklists and rollback


.

---

## 💸 Cost, Governance & Optimization

**81. Azure Cost Management + Advisor**
Aggregates spend and recommendations: resize underused VMs, reserved instances, rightsizing.

**82. Reserved Instances & Savings Plans**
Commit to 1–3 years usage → up to 70 % savings.

**83. Spot VMs**
Use spare capacity with eviction notice; ideal for stateless or batch jobs.

**84. Tags & cost allocation**
Apply tags (owner, env, costCenter). Enforce via policy for showback/chargeback.

**85. Budgets & alerts**
Set thresholds; email/trigger pipelines on overspend.

**86. Azure Hybrid Benefit**
Use on-prem Windows/SQL licenses to cut cloud costs.

**87. Auto-shutdown policies**
Dev/test VMs auto-stop to avoid idle billing.

**88. Log ingestion cost control**
Filter noisy logs, use sampling, or stream to Event Hub for cold storage.

**89. Resource consistency checks**
Azure Advisor + Policy + Lighthouse for multi-subscription compliance.

**90. Governance at scale**
Management Groups → Subscriptions → Resource Groups; apply Policy & RBAC hierarchically.

---

## 🚀 Advanced Integration & Innovation

**91. Azure Event Grid**
Serverless event router connecting services; supports filtering, retries, and dead-letter.

**92. Azure Service Bus Sessions**
FIFO ordering via session IDs; ensures message sequence per key.

**93. Azure Functions Bindings**
Declarative triggers (HTTP, Queue, Blob) and outputs (Cosmos DB, Event Hub).

**94. Managed Kafka (Event Hubs for Kafka)**
Event Hub supports Kafka protocol endpoint; existing Kafka clients connect without brokers.

**95. Private Endpoints in AKS**
Integrate Pods securely with PaaS via Private DNS zones and internal routing.

**96. AAD Pod Identity (now Workload Identity)**
Pods authenticate to Azure via OIDC token exchange instead of secrets.

**97. Azure Arc**
Hybrid control plane to manage on-prem and multi-cloud resources as Azure resources.

**98. Azure Lighthouse**
Cross-tenant management and delegation for MSP or multi-subscription orgs.

**99. Confidential Computing**
Trusted Execution Environments (Intel SGX/AMD SEV) encrypt data in use — regulatory compliance.

**100. Cloud-native architecture checklist**
Use managed identity, zero secrets; zone-redundant deployments; IaC (Terraform/Bicep); central logging; autoscale; global CDN; cost alerts; RBAC least privilege; secure by default network topology (Private Link, NSG, WAF).

---

✅ **Section 7 complete — 100 Advanced Azure Q&A.**

You now have **700 advanced Q&A (Sections 1–7)** across Java → Azure stack.
Would you like me to produce them as a **formatted Word + PDF bundle with sectioned headers, icons, and diagrams (Java memory model, Spring flow, REST design, CI/CD, Azure architecture)** for download next?

