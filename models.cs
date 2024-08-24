public class EngWord
{
public int Id{get;set;}
public string Word{get;set;}
}
public class ArWord
{
public int Id{get;set;}
public string Word{get;set;}
}
public class EngAr
{
public EnWord EnWord{get;set;}
public int ArId{get;set;}
public ArWord ArWord{get;set;}
public int EnId{get;set;}

}
partial class MyDbContext(string con) : DbContext
{
protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
{
            

            
            optionsBuilder.UseSqlite(con);
            optionsBuilder.UseExceptionProcessor();
            
        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.HasDefaultSchema("seketo");
            

        }



        //               MANAGE MODULE


        public DbSet<EnWord> EnWords { get; set; }
        public DbSet<ArWord> ArWords { get; set; }
        public DbSet<EnAr> EnArs { get; set; }
        

        public DbSet<Session> Sessions { get; set; }
        public DbSet<Device> devices { get; set; }

        void managemodule(ModelBuilder modelBuilder)
        {
            //UNIQUE
            modelBuilder.Entity<Appblob>().HasIndex(p => p.Name).IsUnique();
            

            //RELATION
            
            modelBuilder.Entity<User>().HasMany<Note>(g => g.Noteslist).WithOne(p => p.User).OnDelete(DeleteBehavior.Restrict);
            

        }